import random, sys

list_of_training = [
    "HYPERTROPHY",
    "STRENGTH",
    "ENDURANCE",
]

# Selecting the type of trianing you'll ike to do NOTE: this will defer the different reps, sets and rest
def type_of_training():
    while True:
        print("Please select the Type of Training: ", list_of_training)
        training = (input()).upper().strip()
        if training in list_of_training:
            print(f"Type of training selected {training}")
            return training
        else:
            print("Invalid Type of Training.")

list_of_muscles = [
    "CHEST",
    "BACK",
    "SHOULDERS",
    "ARMS",
    "LEGS",
    "FULL BODY",
]

# Target muscle of what workout you'll like to do
def target_muscle():
    while True:
        print("Please select the target muscle for exercise: ", list_of_muscles)
        target_muscle_selected = input().upper().strip()
        if target_muscle_selected in list_of_muscles:
            print(f"Target Muscle Selected: {target_muscle_selected}")
            return target_muscle_selected
        else:
            print("Muscle type not in the list, try again.")

# === Just a list of workouts ===

list_of_chest = [
    "Bench Press",
    "Push-Ups",
    "Chest Flyes",
    "Chest Press Machine",
    "Cable Crossovers",
    "Pec Deck Machine",
    "Incline Dumbbell Press",
    "Landmine Press",
]

list_of_back = [
    "Lat Pulldowns",
    "Deadlifts",
    "Bent-Over-Rows",
    "Seated Cable Rows",
    "T-Bar Rows",
    "Single-Arm Dumbbell Rows",
    "Face Pulls",
    "Hyperextensions",
    "Inverted Rows",
    "Pull-Ups",
]

list_of_arms = [
    "Bicep Curls",
    "Tricep Dips",
    "Skull Crushers",
    "Concenration Curls",
    "Tricep Pushdowns",
    "Preacher Curls",
    "Overhead Tricep Extension",
    "Close-Grip Bench Press",
    "Reverse Curls"
    "Kickbacks"
]

list_of_shoulder = [
    "Overhead Press",
    "Lateral Raise",
    "Front Raises",
    "Rear Delt Flyes",
    "Arnold Press",
    "Upright Rows",
    "Face Pulls",
    "Shrugs",
    "Push Press",
    "Single-Arm Cable Lateral Raises"
]

list_of_legs = [
    "Squats",
    "Deadlifts",
    "Lunges",
    "Leg Press",
    "Leg Curls",
    "Leg Exnensions",
    "Calf Raise",
    "Hip Thrusts",
    "Step-Ups",
    "Glute Bridges",
]

list_of_fullbody = list_of_chest + list_of_back + list_of_arms + list_of_shoulder + list_of_legs

muscle_to_exercises = {
    "CHEST": list_of_chest,
    "BACK": list_of_back,
    "ARM": list_of_arms,
    "SHOULDER": list_of_shoulder,
    "LEGS": list_of_legs,
    "FULL BODY": list_of_fullbody
}

def pick_random_workouts(target_muscle):
    exercises = muscle_to_exercises[target_muscle]
    selected_exercises = random.sample(exercises, 4)
    return selected_exercises

training = type_of_training()
target_muscle_selected = target_muscle()
workouts = pick_random_workouts(target_muscle_selected)

print(f"Selected workouts for {target_muscle_selected}: {workouts}")

def display_training():
    if training == "HYPERTROPHY":
        print("SETS: 3 | REPS: 8 - 10 | Rest: 60 seconds")
        print("NOTE: 60% - 80% of 1-RM")
    elif training == "STRENGTH":
        print("SETS: 3 | REPS: 3 - 5 | Rest: 60 - 90 seconds")
        print("NOTE: 85% - 100% of 1-RM")
    elif training == "ENDURANCE":
        print("SETS: 3 | REPS: 14 - 18 | Rest: 60 seconds")
        print("NOTE: 30% - 60% of 1-RM")

display_training()
# By Cy "still new to python, ye