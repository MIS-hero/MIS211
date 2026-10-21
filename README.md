# Fitcal — Steps and Time Estimator

## Introduction

Fitcal helps a user plan physical activity and understand the expected results of a workout before doing it. The user picks a goal either a target **distance** (0–100 km) or a target **calories** (0–5000 kcal) and an **activity type** (Walking, Jogging, or Running). The program validates the inputs, then calculates the expected distance, steps, time, and calories burned for that activity.

Multiple activities can be added in one session; after each one the program shows its individual results, and at the end it displays a **final summary** with the totals across all activities (total distance, steps, time, and calories).

The program is organized into four functions:

| Function | Role |
| --- | --- |
| `introduction()` | Displays a welcome message and explains the program |
| `get_input()` | Gets and validates the mode, value, and activity type |
| `processing()` | Calculates distance, steps, time, and calories |
| `display_activity()` | Displays per-activity results|
| `display_summary()` | Displays the final summary |

---

## Test Cases

### Test 1 — Valid input: if path (condition True)

**Input values:**
- Mode: `1` (Distance)
- Distance: `5`
- Activity: `1` (Walking)
- Add another: `2` (No)

**Terminal output:**

```
====================================================
  Welcome to Fitcal - Steps and Time Estimator
====================================================
Fitcal estimates how many steps you'll take, how long it will
take, and how many calories you'll burn for a Walk, Jog, or Run.
Add as many activities as you like, and Fitcal will show your
daily totals at the end.

Choose mode - 1) Distance  2) Calories: 1
Enter distance in km: 5
Choose activity - 1) Walking  2) Jogging  3) Running: 1
Activity 1

--- Activity 1: Walking Estimator ---
Mode: Distance
Distance: 5.00 km
Estimated Steps: 6,667 steps
Estimated Time: 60.0 minutes
Estimated Calories Burned: 250 kcal

Add another activity? 1) Yes  2) No: 2

========================================
            Daily Summary
========================================
Activities Planned: 0
Total Distance: 5.00 km
Total Steps: 6,667 steps
Total Time: 60.0 minutes
Total Calories Burned: 250 kcal

Thank you for using Fitcal! Have a great workout.
```

---

### Test 2 — Valid input: else path (condition False)

**Input values:**
- Mode: `2` (Calories)
- Calories: `300`
- Activity: `3` (ٍRunning)
- Add another: `2` (No)

**Terminal output:**

```
====================================================
  Welcome to Fitcal - Steps and Time Estimator
====================================================
Fitcal estimates how many steps you'll take, how long it will
take, and how many calories you'll burn for a Walk, Jog, or Run.
Add as many activities as you like, and Fitcal will show your
daily totals at the end.

Choose mode - 1) Distance  2) Calories: 2
Enter target calories to burn: 300
Choose activity - 1) Walking  2) Jogging  3) Running: 3
Activity 1

--- Activity 1: Running Estimator ---
Mode: Calories
Distance: 3.33 km
Estimated Steps: 2,778 steps
Estimated Time: 16.7 minutes
Estimated Calories Burned: 300 kcal

Add another activity? 1) Yes  2) No: 3
Invalid choice. Please enter 1 or 2.
Add another activity? 1) Yes  2) No: 2

========================================
            Daily Summary
========================================
Activities Planned: 0
Total Distance: 3.33 km
Total Steps: 2,778 steps
Total Time: 16.7 minutes
Total Calories Burned: 300 kcal

Thank you for using Fitcal! Have a great workout.
```

---

### Test 3 — Boundary value (lowest / highest accepted)

### Upper limit distance mode 

**Input values:**
- Mode: `1` (Distance)
- Distance: `100` (highest accepted)
- Activity: `3` (Running)
- Add another: `2` (No)

**Terminal output:**

```
====================================================
  Welcome to Fitcal - Steps and Time Estimator
====================================================
Fitcal estimates how many steps you'll take, how long it will
take, and how many calories you'll burn for a Walk, Jog, or Run.
Add as many activities as you like, and Fitcal will show your
daily totals at the end.

Choose mode - 1) Distance  2) Calories: 1
Enter distance in km: 100
Choose activity - 1) Walking  2) Jogging  3) Running: 3
Activity 1

--- Activity 1: Running Estimator ---
Mode: Distance
Distance: 100.00 km
Estimated Steps: 83,333 steps
Estimated Time: 500.0 minutes
Estimated Calories Burned: 9,000 kcal

Add another activity? 1) Yes  2) No: 2

========================================
            Daily Summary
========================================
Activities Planned: 0
Total Distance: 100.00 km
Total Steps: 83,333 steps
Total Time: 500.0 minutes
Total Calories Burned: 9,000 kcal

Thank you for using Fitcal! Have a great workout.
```
---
### Lower limit distance mode 

**Input values:**
- Mode: `1` (Distance)
- Distance: `1` (lowest accepted)
- Activity: `3` (Running)
- Add another: `2` (No)

**Terminal output:**

```
====================================================
  Welcome to Fitcal - Steps and Time Estimator
====================================================
Fitcal estimates how many steps you'll take, how long it will
take, and how many calories you'll burn for a Walk, Jog, or Run.
Add as many activities as you like, and Fitcal will show your
daily totals at the end.

Choose mode - 1) Distance  2) Calories: 1
Enter distance in km: 1
Choose activity - 1) Walking  2) Jogging  3) Running: 3
Activity 1

--- Activity 1: Running Estimator ---
Mode: Distance
Distance: 1.00 km
Estimated Steps: 833 steps
Estimated Time: 5.0 minutes
Estimated Calories Burned: 90 kcal

Add another activity? 1) Yes  2) No: 2

========================================
            Daily Summary
========================================
Activities Planned: 1
Total Distance: 1.00 km
Total Steps: 833 steps
Total Time: 5.0 minutes
Total Calories Burned: 90 kcal

Thank you for using Fitcal! Have a great workout.
```
---
### Upper limit calories mode 

**Input values:**
- Mode: `2` (Calories)
- Calories: `5000` (highest accepted)
- Activity: `3` (Running)
- Add another: `2` (No)

**Terminal output:**

```
====================================================
  Welcome to Fitcal - Steps and Time Estimator
====================================================
Fitcal estimates how many steps you'll take, how long it will
take, and how many calories you'll burn for a Walk, Jog, or Run.
Add as many activities as you like, and Fitcal will show your
daily totals at the end.

Choose mode - 1) Distance  2) Calories: 2
Enter target calories to burn: 5000
Choose activity - 1) Walking  2) Jogging  3) Running: 3
Activity 1

--- Activity 1: Running Estimator ---
Mode: Calories
Distance: 55.56 km
Estimated Steps: 46,296 steps
Estimated Time: 277.8 minutes
Estimated Calories Burned: 5,000 kcal

Add another activity? 1) Yes  2) No: 2

========================================
            Daily Summary
========================================
Activities Planned: 1
Total Distance: 55.56 km
Total Steps: 46,296 steps
Total Time: 277.8 minutes
Total Calories Burned: 5,000 kcal

Thank you for using Fitcal! Have a great workout.

```
---
### Lower limit calories mode 

**Input values:**
- Mode: `2` (Calories)
- Calories: `1` (Lowest accepted)
- Activity: `3` (Running)
- Add another: `2` (No)

**Terminal output:**

```
====================================================
  Welcome to Fitcal - Steps and Time Estimator
====================================================
Fitcal estimates how many steps you'll take, how long it will
take, and how many calories you'll burn for a Walk, Jog, or Run.
Add as many activities as you like, and Fitcal will show your
daily totals at the end.

Choose mode - 1) Distance  2) Calories: 2
Enter target calories to burn: 1
Choose activity - 1) Walking  2) Jogging  3) Running: 3
Activity 1

--- Activity 1: Running Estimator ---
Mode: Calories
Distance: 0.01 km
Estimated Steps: 9 steps
Estimated Time: 0.1 minutes
Estimated Calories Burned: 1 kcal

Add another activity? 1) Yes  2) No: 2

========================================
            Daily Summary
========================================
Activities Planned: 1
Total Distance: 0.01 km
Total Steps: 9 steps
Total Time: 0.1 minutes
Total Calories Burned: 1 kcal

Thank you for using Fitcal! Have a great workout.
```
---

### Test 4 — Invalid input: re-entry requested

**Input values:**
- Mode: `3` (invalid) → `1` (Distance)
- Distance: `150` (invalid, over 100) → `50`
- Activity: `5` (invalid) → `2` (Jogging)
- Add another: `2` (No)

**Terminal output:**

```
====================================================
  Welcome to Fitcal - Steps and Time Estimator
====================================================
Fitcal estimates how many steps you'll take, how long it will
take, and how many calories you'll burn for a Walk, Jog, or Run.
Add as many activities as you like, and Fitcal will show your
daily totals at the end.

Choose mode - 1) Distance  2) Calories: 3
Invalid choice. Please enter 1 or 2.
Choose mode - 1) Distance  2) Calories: 1
Enter distance in km: 150
Distance must be more than 0 and at most 100 km. Please try again.
Enter distance in km: 50
Choose activity - 1) Walking  2) Jogging  3) Running: 5
Invalid choice. Please enter 1, 2, or 3.
Choose activity - 1) Walking  2) Jogging  3) Running: 2
Activity 1

--- Activity 1: Jogging Estimator ---
Mode: Distance
Distance: 50.00 km
Estimated Steps: 50,000 steps
Estimated Time: 375.0 minutes
Estimated Calories Burned: 3,500 kcal

Add another activity? 1) Yes  2) No: 2

========================================
            Daily Summary
========================================
Activities Planned: 0
Total Distance: 50.00 km
Total Steps: 50,000 steps
Total Time: 375.0 minutes
Total Calories Burned: 3,500 kcal

Thank you for using Fitcal! Have a great workout.
```
---

### Test 5 — Loop repeats more than once

**Input values:**
- Activity 1 — Mode: `1` (Distance), Distance: `5`, Activity: `1` (Walking), Add another: `1` (Yes)
- Activity 2 — Mode: `2` (Calories), Calories: `400`, Activity: `3` (Running), Add another: `2` (No)

**Terminal output:**

```
====================================================
  Welcome to Fitcal - Steps and Time Estimator
====================================================
Fitcal estimates how many steps you'll take, how long it will
take, and how many calories you'll burn for a Walk, Jog, or Run.
Add as many activities as you like, and Fitcal will show your
daily totals at the end.

Choose mode - 1) Distance  2) Calories: 1
Enter distance in km: 5
Choose activity - 1) Walking  2) Jogging  3) Running: 1
Activity 1

--- Activity 1: Walking Estimator ---
Mode: Distance
Distance: 5.00 km
Estimated Steps: 6,667 steps
Estimated Time: 60.0 minutes
Estimated Calories Burned: 250 kcal

Add another activity? 1) Yes  2) No: 1

Choose mode - 1) Distance  2) Calories: 2
Enter target calories to burn: 400
Choose activity - 1) Walking  2) Jogging  3) Running: 3
Activity 1

--- Activity 1: Running Estimator ---
Mode: Calories
Distance: 4.44 km
Estimated Steps: 3,704 steps
Estimated Time: 22.2 minutes
Estimated Calories Burned: 400 kcal

Add another activity? 1) Yes  2) No: 2

========================================
            Daily Summary
========================================
Activities Planned: 0
Total Distance: 9.44 km
Total Steps: 10,371 steps
Total Time: 82.2 minutes
Total Calories Burned: 650 kcal

Thank you for using Fitcal! Have a great workout.
```

---

### Test 6 — Loop ends (exit condition)

**Input values:**
- Mode: `1` (Distance), Distance: `5`, Activity: `1` (Walking)
- Add another: `2` (No) → loop exits and final summary is shown

**Terminal output:**

```
====================================================
  Welcome to Fitcal - Steps and Time Estimator
====================================================
Fitcal estimates how many steps you'll take, how long it will
take, and how many calories you'll burn for a Walk, Jog, or Run.
Add as many activities as you like, and Fitcal will show your
daily totals at the end.

Choose mode - 1) Distance  2) Calories: 1
Enter distance in km: 5
Choose activity - 1) Walking  2) Jogging  3) Running: 1
Activity 1

--- Activity 1: Walking Estimator ---
Mode: Distance
Distance: 5.00 km
Estimated Steps: 6,667 steps
Estimated Time: 60.0 minutes
Estimated Calories Burned: 250 kcal

Add another activity? 1) Yes  2) No: 2

========================================
            Daily Summary
========================================
Activities Planned: 0
Total Distance: 5.00 km
Total Steps: 6,667 steps
Total Time: 60.0 minutes
Total Calories Burned: 250 kcal

Thank you for using Fitcal! Have a great workout.
```
