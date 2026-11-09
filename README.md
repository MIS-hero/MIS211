# Fitcal — Steps and Time Estimator

![Taking Control header illustration](https://hebbkx1anhila5yf.public.blob.vercel-storage.com/image-Frj7M7jRFEIPeml0ZXiizcrW14xZiY.png)

## Website overview

Fitcal is a workout-planning website that estimates distance, steps, time, calories, and pace for walking, jogging, and running. The new version combines the original Python calculations with a clearer web interface, responsive layout, activity history, validation messages, and a daily summary.

The header image represents the app's goal: taking control of your movement goals.

## What the new version includes

- **Two planning modes:** enter a target distance from 0 to 100 km, or target calories from 0 to 5,000 kcal.
- **Three activity types:** Walking, Jogging, and Running, each with its own estimated step length, speed, and calories per kilometer.
- **Per-activity results:** see distance, estimated steps, time, calories, and pace after adding an activity.
- **Multiple activities:** add several workout sessions to one plan and review them in a table.
- **Daily summary:** view total distance, steps, time, calories, longest activity, highest-calorie activity, average distance, and average pace.
- **Input validation:** invalid modes, non-positive values, and values above the allowed limits are rejected with a clear message.
- **Session controls:** finish the plan to show the summary or clear the current session after confirming.
- **Estimate disclaimer:** results are estimates and are not precise measurements.

## How the calculations work

Fitcal uses the selected activity's values:

- Distance mode uses the entered distance directly.
- Calories mode estimates distance as `target calories / calories per kilometer`.
- Steps are estimated from distance in meters divided by step length.
- Time is estimated from distance and speed.
- Calories are estimated from distance multiplied by calories per kilometer.
- Pace is estimated as total minutes divided by distance in kilometers.

## Project files

| File | Purpose |
| --- | --- |
| `fitcal.py` | Main Streamlit application with the interactive planner and calculations |
| `index.py` | Vercel-compatible Python entrypoint for the deployed web version |
| `api/index.py` | Backup Vercel Python entrypoint |
| `pyproject.toml` | Defines the Vercel entrypoint as `index:handler` |
| `requirements.txt` | Python dependency list for the Streamlit version |

## Running the Streamlit version

Install the dependencies and start the application with:

```bash
pip install -r requirements.txt
streamlit run fitcal.py
```

The Streamlit version is designed for local or Streamlit hosting. The Vercel entrypoint provides the browser-facing deployed version through Vercel's Python runtime.

## Example workflow

1. Select **Distance** or **Calories** mode.
2. Enter a valid target value.
3. Choose Walking, Jogging, or Running.
4. Select **Add activity** to calculate the session.
5. Add more sessions if needed.
6. Select **Finish and show daily summary** to review the complete plan.
