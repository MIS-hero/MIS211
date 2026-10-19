"""
Fitcal - Steps and Time Estimator (Daily Planner)
-------------------------------------------------
Fitcal estimates the steps, time, and calories burned for a Walking,
Jogging, or Running session. For each activity the user picks a mode:
  1) Distance mode - enter a distance in km.
  2) Calories mode - enter a calorie target, and Fitcal works out the
                     distance needed based on the chosen activity.
The user can add as many activities as they like. When they finish,
Fitcal displays a daily summary of the totals for all activities.
"""

# ---------------------------------------------------------------------------
# Named constants: step length (meters), speed (km/h), calories burned
# per kilometer. Typical planning estimates for an average adult at a
# moderate pace (see Sheet 2 for the reference ranges).
# ---------------------------------------------------------------------------
WALKING_STEP_LENGTH_METERS = 0.75   # avg. adult step length (~0.7-0.8 m)
WALKING_SPEED_KMH = 5               # moderate/brisk walking pace (~4-6 km/h)
WALKING_CALORIES_PER_KM = 50        # avg. adult, brisk pace (~30-60 kcal/km)

JOGGING_STEP_LENGTH_METERS = 1.0    # step lengthens as pace picks up
JOGGING_SPEED_KMH = 8               # light jogging pace (~6-8 km/h)
JOGGING_CALORIES_PER_KM = 70        # between walking and running (~60-85 kcal/km)

RUNNING_STEP_LENGTH_METERS = 1.2    # running step length (~1.1-1.6 m)
RUNNING_SPEED_KMH = 12              # recreational running pace (~8-12 km/h)
RUNNING_CALORIES_PER_KM = 90        # avg. adult, recreational run (~60-110 kcal/km)

# Realistic upper limits for a single activity (used by input validation).
# 5,000 kcal is exactly 100 km of walking (100 x 50 kcal/km), so both
# limits describe the same "longest realistic single activity".
MAX_DISTANCE_KM = 100
MAX_CALORIES = 5000

# ---------------------------------------------------------------------------
# Accumulators for the daily summary (start at 0 before the loop)
# ---------------------------------------------------------------------------
total_distance_km = 0.0
total_steps = 0.0
total_time_minutes = 0.0
total_calories = 0.0
activity_count = 0      # counts how many activities have been added

# ---------------------------------------------------------------------------
# Welcome message
# ---------------------------------------------------------------------------
print("=" * 52)
print("  Welcome to Fitcal - Steps and Time Estimator")
print("=" * 52)
print(
    "Fitcal estimates how many steps you'll take, how long it will\n"
    "take, and how many calories you'll burn for a Walk, Jog, or Run.\n"
    "Add as many activities as you like, and Fitcal will show your\n"
    "daily totals at the end.\n"
)

# ---------------------------------------------------------------------------
# Main loop: repeats once for each activity the user adds.
# add_another starts as "1" so the loop runs at least once.
# ---------------------------------------------------------------------------
add_another = "1"

while add_another == "1":

    # Count this activity (used to number the results and in the summary)
    activity_count += 1
    print(f"Activity {activity_count}")

    # Step 1: Choose mode (validated - only "1" or "2" accepted)
    mode_choice = input("Choose mode - 1) Distance  2) Calories: ").strip()
    while mode_choice != "1" and mode_choice != "2":
        print("Invalid choice. Please enter 1 or 2.")
        mode_choice = input("Choose mode - 1) Distance  2) Calories: ").strip()

    if mode_choice == "1":
        mode_name = "Distance"
    else:
        mode_name = "Calories"

    # Step 2: Collect the mode-specific input
    # (validated - must be greater than 0 and not above the realistic limit)
    if mode_choice == "1":
        distance_km = float(input("Enter distance in km: "))
        while distance_km <= 0 or distance_km > MAX_DISTANCE_KM:
            print(f"Distance must be more than 0 and at most {MAX_DISTANCE_KM} km. Please try again.")
            distance_km = float(input("Enter distance in km: "))
    else:
        target_calories = float(input("Enter target calories to burn: "))
        while target_calories <= 0 or target_calories > MAX_CALORIES:
            print(f"Calories must be more than 0 and at most {MAX_CALORIES} kcal. Please try again.")
            target_calories = float(input("Enter target calories to burn: "))

    # Step 3: Choose activity (validated - only "1", "2", or "3" accepted)
    activity_choice = input(
        "Choose activity - 1) Walking  2) Jogging  3) Running: "
    ).strip()
    while activity_choice != "1" and activity_choice != "2" and activity_choice != "3":
        print("Invalid choice. Please enter 1, 2, or 3.")
        activity_choice = input(
            "Choose activity - 1) Walking  2) Jogging  3) Running: "
        ).strip()

    if activity_choice == "1":
        activity_name = "Walking"
        step_length_meters = WALKING_STEP_LENGTH_METERS
        speed_kmh = WALKING_SPEED_KMH
        calories_per_km = WALKING_CALORIES_PER_KM
    elif activity_choice == "2":
        activity_name = "Jogging"
        step_length_meters = JOGGING_STEP_LENGTH_METERS
        speed_kmh = JOGGING_SPEED_KMH
        calories_per_km = JOGGING_CALORIES_PER_KM
    else:
        activity_name = "Running"
        step_length_meters = RUNNING_STEP_LENGTH_METERS
        speed_kmh = RUNNING_SPEED_KMH
        calories_per_km = RUNNING_CALORIES_PER_KM

    # Step 4: In Calories mode, work out the distance now that the
    # activity's calorie rate is known.
    if mode_choice == "2":
        distance_km = target_calories / calories_per_km

    # Step 5: Apply the required formulas, in order
    distance_m = distance_km * 1000
    steps = distance_m / step_length_meters
    time_hours = distance_km / speed_kmh
    time_minutes = time_hours * 60
    calories_burned = distance_km * calories_per_km

    # Step 6: Print this activity's results
    print(f"\n--- Activity {activity_count}: {activity_name} Estimator ---")
    print(f"Mode: {mode_name}")
    print(f"Distance: {distance_km:.2f} km")
    print(f"Estimated Steps: {steps:,.0f} steps")
    print(f"Estimated Time: {time_minutes:.1f} minutes")
    print(f"Estimated Calories Burned: {calories_burned:,.0f} kcal\n")

    # Step 7: Add this activity's results to the daily running totals.
    # Steps are whole counts, so the rounded value is added - this way the
    # total always equals the sum of the step counts shown for each activity.
    total_distance_km += distance_km
    total_steps += round(steps)
    total_time_minutes += time_minutes
    total_calories += calories_burned

    # Step 8: Ask whether to add another activity (validated - "1" or "2")
    add_another = input("Add another activity? 1) Yes  2) No: ").strip()
    while add_another != "1" and add_another != "2":
        print("Invalid choice. Please enter 1 or 2.")
        add_another = input("Add another activity? 1) Yes  2) No: ").strip()
    print()

# ---------------------------------------------------------------------------
# Daily summary (displayed once, after the loop ends)
# ---------------------------------------------------------------------------
print("=" * 40)
print("            Daily Summary")
print("=" * 40)
print(f"Activities Planned: {activity_count}")
print(f"Total Distance: {total_distance_km:.2f} km")
print(f"Total Steps: {total_steps:,.0f} steps")
print(f"Total Time: {total_time_minutes:.1f} minutes")
print(f"Total Calories Burned: {total_calories:,.0f} kcal")
print("\nThank you for using Fitcal! Have a great workout.")
