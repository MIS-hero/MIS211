"""Fitcal - Steps and Time Estimator, built with Streamlit."""

import math
from typing import Any

import streamlit as st


MAX_DISTANCE_KM = 100.0
MAX_CALORIES = 5000.0

# ACTIVITIES stores the step length, speed, and calories per kilometer for each activity.
ACTIVITIES = {
    "Walking": {"step_length": 0.75, "speed": 5.0, "calories_per_km": 50.0},
    "Jogging": {"step_length": 1.0, "speed": 8.0, "calories_per_km": 70.0},
    "Running": {"step_length": 1.2, "speed": 12.0, "calories_per_km": 90.0},
}

HEADER_IMAGE_URL = "https://hebbkx1anhila5yf.public.blob.vercel-storage.com/image-Frj7M7jRFEIPeml0ZXiizcrW14xZiY.png"

DESCRIPTION = (
    "Fitcal estimates how many steps you'll take, how long it will take, "
        "and how many calories you'll burn for a Walk, Jog, or Run. Add as many "
        "activities as you like, and Fitcal will show your daily totals at the end. "
        "Calories, time, and steps are estimates, not precise measurements."

)


def format_time(total_minutes: int) -> str:
    """Format rounded minutes as minutes or hours plus minutes."""
    if total_minutes < 60:
        return f"{total_minutes} minutes"
    hours, minutes = divmod(total_minutes, 60)
    hour_label = "hour" if hours == 1 else "hours"
    return f"{hours} {hour_label} {minutes} minutes"


# calculate_activity() calculates distance, steps, time, and calories for one activity.
def calculate_activity(mode: str, value: float, activity_name: str) -> dict[str, Any]:
    """Calculate one activity using the flowchart formulas."""
    activity = ACTIVITIES[activity_name]
    distance_km = value if mode == "Distance" else value / activity["calories_per_km"]
    steps = round((distance_km * 1000) / activity["step_length"])
    total_minutes = round((distance_km / activity["speed"]) * 60)
    calories = round(distance_km * activity["calories_per_km"])
    pace_minutes_per_km = total_minutes / distance_km if distance_km else 0
    return {
        "activity": activity_name,
        "mode": mode,
        "distance_km": distance_km,
        "steps": steps,
        "time_minutes": total_minutes,
        "time_display": format_time(total_minutes),
        "pace_minutes_per_km": pace_minutes_per_km,
        "pace_display": f"{pace_minutes_per_km:.1f} min/km",
        "calories": calories,
    }


def initialize_state() -> None:
    """Create the session values used to keep activities between clicks."""
    if "activities" not in st.session_state:
        st.session_state.activities = []
    if "last_activity" not in st.session_state:
        st.session_state.last_activity = None
    if "show_summary" not in st.session_state:
        st.session_state.show_summary = False


def render_activity_result(activity: dict[str, Any]) -> None:
    """Render the most recently added activity."""
    st.subheader("Activity result")
    st.success(f"Activity {len(st.session_state.activities)} added successfully.")
    with st.container(border=True):
        st.markdown(f"### {activity['activity']} session")
        st.write(f"**Mode:** {activity['mode']}")
        st.write(f"**Distance:** {activity['distance_km']:.2f} km")
        st.write(f"**Estimated steps:** {activity['steps']:,} steps")
        st.write(f"**Estimated time:** {activity['time_display']}")
        st.write(f"**Pace:** {activity['pace_display']}")
        st.write(f"**Estimated calories:** {activity['calories']:,} kcal")
        st.caption("Calories, time, and steps are estimates, not precise measurements.")


def render_activity_table() -> None:
    """Render every activity added during this session."""
    st.subheader("Your activities")
    if not st.session_state.activities:
        st.info("No activities yet.")
        return

    rows = [
        {
            "#": index,
            "Activity": item["activity"],
            "Mode": item["mode"],
            "Distance": f"{item['distance_km']:.2f} km",
            "Steps": f"{item['steps']:,} steps",
            "Time": item["time_display"],
            "Pace": item["pace_display"],
            "Calories": f"{item['calories']:,} kcal",
        }
        for index, item in enumerate(st.session_state.activities, start=1)
    ]
    st.table(rows)


def render_daily_summary() -> None:
    """Render totals after the user finishes planning."""
    if not st.session_state.show_summary:
        return

    st.subheader("Daily Summary")
    activities = st.session_state.activities
    if not activities:
        st.warning("Add at least one activity before finishing.")
        return

    total_distance = sum(item["distance_km"] for item in activities)
    total_steps = sum(item["steps"] for item in activities)
    total_minutes = sum(item["time_minutes"] for item in activities)
    total_calories = sum(item["calories"] for item in activities)
    longest_activity = max(activities, key=lambda item: item["distance_km"])
    highest_calorie_activity = max(activities, key=lambda item: item["calories"])
    average_distance = total_distance / len(activities)
    average_pace = total_minutes / total_distance if total_distance else 0

    columns = st.columns(5)
    metrics = [
        ("Activities", f"{len(activities)}"),
        ("Distance", f"{total_distance:.2f} km"),
        ("Steps", f"{total_steps:,}"),
        ("Time", format_time(total_minutes)),
        ("Calories", f"{total_calories:,} kcal"),
    ]
    # This for loop displays each total as a separate metric.
    for column, (label, value) in zip(columns, metrics):
        column.metric(label, value)
    details = st.columns(4)
    details[0].metric("Longest activity", f"{longest_activity['activity']} ({longest_activity['distance_km']:.2f} km)")
    details[1].metric("Most calories", f"{highest_calorie_activity['activity']} ({highest_calorie_activity['calories']:,} kcal)")
    details[2].metric("Average distance", f"{average_distance:.2f} km/activity")
    details[3].metric("Average pace", f"{average_pace:.1f} min/km")
    st.caption("All calories, time, steps, and pace values are estimates, not precise measurements.")
    st.success("Daily summary complete. Thank you for using Fitcal! Have a great workout.")


def render_plan_form() -> None:
    """Render inputs and validate a new activity."""
    st.subheader("Plan an activity")
    mode = st.radio("Calculation mode", ["Distance", "Calories"], horizontal=True)

    with st.form("activity_form", clear_on_submit=False):
        if mode == "Distance":
            value = st.number_input(
                "Distance (km)", min_value=0.0, value=5.0, step=0.1, format="%.2f"
            )
        else:
            value = st.number_input(
                "Target calories (kcal)", min_value=0.0, value=300.0, step=10.0, format="%.0f"
            )
        activity_name = st.selectbox("Activity type", list(ACTIVITIES), index=0)
        add_clicked = st.form_submit_button("Add activity", type="primary", use_container_width=True)

    if not add_clicked:
        return

    if mode not in {"Distance", "Calories"}:
        st.error("Please choose a calculation mode: Distance or Calories.")
        return
    # This if statement checks whether the entered distance is within the valid range (0 < distance <= 100).
    if mode == "Distance" and (not math.isfinite(value) or value <= 0 or value > MAX_DISTANCE_KM):
        st.error("Distance must be more than 0 and at most 100 km. Please try again.")
        return
    if mode == "Calories" and (not math.isfinite(value) or value <= 0 or value > MAX_CALORIES):
        st.error("Calories must be more than 0 and at most 5000 kcal. Please try again.")
        return
    if activity_name not in ACTIVITIES:
        st.error("Please choose an activity: Walking, Jogging, or Running.")
        return

    result = calculate_activity(mode, value, activity_name)
    st.session_state.activities.append(result)
    st.session_state.last_activity = result
    st.session_state.show_summary = False
    st.rerun()


def main() -> None:
    st.set_page_config(page_title="Fitcal - Steps and Time Estimator", page_icon="🏃", layout="centered")
    initialize_state()
    st.image(HEADER_IMAGE_URL, caption="Taking control of your movement goals", use_container_width=True)
    st.title("Fitcal - Steps and Time Estimator")
    st.write(DESCRIPTION)
    st.info("Note: calories, time, steps, and pace are estimates, not precise measurements.")

    render_plan_form()
    if st.session_state.last_activity:
        render_activity_result(st.session_state.last_activity)
    render_activity_table()

    finish, clear = st.columns(2)
    with finish:
        if st.button("Finish and show daily summary", use_container_width=True):
            st.session_state.show_summary = True
    with clear:
        confirm_clear = st.checkbox("Confirm starting a new session", key="confirm_clear")
        if st.button("Clear all activities", disabled=not confirm_clear, use_container_width=True):
            st.session_state.activities = []
            st.session_state.last_activity = None
            st.session_state.show_summary = False
            st.success("All activities cleared.")

    render_daily_summary()


if __name__ == "__main__":
    main()
