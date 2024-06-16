import random
import sys
import time

print("Welcome to Cy Exercise Generator")
time.sleep(1)

type_of_training_list = {
    "1": "Hypertrophy",
    "2": "Strength",
    "3": "Endurance",
}

def type_of_training():
    while True:
        print("Type of trainings:")
        for key, value in type_of_training_list.items():
            print(f"{key}: {value}")
        try:
            training_selected = int(input("Please select a type of training: "))
            if str(training_selected) in type_of_training_list.keys():
                print(f"Type of training selected: {type_of_training_list[str(training_selected)]}")
                return training_selected
            else:
                print("Invalid Type of Training")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

type_of_training()

difficulty_level = {
    "1": "Beginner",
    "2": "Intermediate",
    "3": "Advanced",
}

def my_difficulty_level():
    while True:
        print("Let's dig deepr and discover your training level")
        time.sleep(1)
        print("We have 3 categories of training difficulty level which are:")
        for key, value in difficulty_level.items():
            print(f"{key}: {value}")
            time.sleep(1)
        print()
        time.sleep(3)
        print("Please answer the following questions to determine your training difficulty level: ")
        print()

        questions = [
            ("Q1: Resistance Training Experience",
            "a. This will be my first experience with structured resistance training. (1 point)",
            "b. I have trained consistently for 6 months to 2 years. (2 points)",
            "c. I have trained consistently for more than 2 years. (3 points)"),
            ("Q2: Recent Training Consistency",
            "a. I have not trained recently, or it has been more than 3 months since I last trained. (1 point)",
            "b. I trained 1-2 weeks ago. (2 points)",
            "c. I currently train 2-4 times per week. (3 points)"),
            ("Q3: General Daily Activity Level",
            "a. I am mostly sedentary (e.g., desk job, little physical activity). (1 point)",
            "b. I am somewhat active (e.g., recreational athlete, regular hikes). (2 points)",
            "c. I am very active (e.g., daily physical exercise, athletic job). (3 points)"),
            ("Q4: Athletic Background",
            "a. I have no athletic background or participation in sports. (1 point)",
            "b. I played more than one sport in high school. (2 points)",
            "c. I participated in college athletics or multiple sports beyond high school. (3 points)"),
            ("Q5: Current Strength Level",
            "a. I cannot perform a proper squat or deadlift with bodyweight, or cannot perform bodyweight chin-ups/push-ups. (1 point)",
            "b. I can perform a squat/deadlift with bodyweight, and multiple chin-ups/push-ups. (2 points)",
            "c. I can perform a squat/deadlift with 1.5 times bodyweight, advanced press, or bench press with bodyweight. (3 points)"),
            ("Q6: Recovery Practices",
            "a. I rarely focus on recovery (e.g., insufficient sleep, no stretching, poor nutrition). (1 point)",
            "b. I occasionally focus on recovery (e.g., irregular sleep, occasional stretching, moderate nutrition). (2 points)",
            "c. I consistently focus on recovery (e.g., regular sleep, daily stretching, balanced nutrition). (3 points)"),
        ]

        answers = []
        for question in questions:
            print(question[0])
            for option in question[1:]:
                print(option)
            while True:
                answer = input("Your answer: ")
                if answer.lower() not in ['a', 'b', 'c']:
                    print("Invalid Answer. Please enter either a, b, or c")
                    continue
                answers.append(answer.lower())
                break
            print()

        score = sum([1 if answer == 'a' else 2 if answer == 'b' else 3 for answer in answers])

        print(f"Your score is: {score}")
        if score <= 10:
            print("Your training difficulty level is Beginner")
        elif 10 < score <= 14:
            print("Your training difficulty level is Intermediate")
        elif score > 14:
            print("Your training difficulty level is Advanced")
        break
    print()

def dyk_difficulty_level():
    while True:
        print("Do you know your training difficulty level?")
        dyk_level = input("(Y/N): ")
        if dyk_level.lower() == "y":
            return
        elif dyk_level.lower() == "n":
            print("Would you like to know your training difficulty level?")
            determine_difficulty_level = input("(Y/N): ")
            if determine_difficulty_level.lower() == "y":
                my_difficulty_level()
                return
            elif determine_difficulty_level.lower() == "n":
                return

dyk_difficulty_level()

def difficulty_level_select():
    while True:
        print("What is your training difficulty level?")
        for key, value in difficulty_level.items():
            print(f"{key}: {value}")
            time.sleep(0.5)
        my_difficulty_level_selected = input("Please select a difficulty level: ")
        if my_difficulty_level_selected in difficulty_level:
            print(f"Difficulty Level Selected: {difficulty_level[my_difficulty_level_selected]}")
            return my_difficulty_level_selected
        else:
            print("Invalid input. Please select a difficulty level.")

difficulty_level_select()

list_of_target_muscles = {
    "1": "Chest",
    "2": "Back",
    "3": "Core",
    "4": "Shoulders",
    "5": "Arms",
    "6": "Legs",
    "7": "Full-body"
}

def target_muscle():
    while True:
        print("Now please select the target muscles for the exercise:")
        for key, value in list_of_target_muscles.items():
            print(f"{key}: {value}")
            time.sleep(0.5)
        try:
            target_muscle_selected = int(input("Please select target muscle: "))
            if str(target_muscle_selected) in list_of_target_muscles.keys():
                print(f"Target muscle selected: {list_of_target_muscles[str(target_muscle_selected)]}")
                return target_muscle_selected
            else:
                print("Invalid input. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

target_muscle()

list_of_place = {
    "1": "Home",
    "2": "Gym",
}

def workout_place_select():
    while True:
        print("Now please select the workout place for the exercise:")
        for key, value in list_of_place.items():
            print(f"{key}: {value}")
            time.sleep(0.5)
        try:
            workout_place_selected = int(input("Please select workout place: "))
            if str(workout_place_selected) in list_of_place.keys():
                print(f"Workout place selected: {list_of_place[str(workout_place_selected)]}")
                return workout_place_selected
            else:
                print("Invalid input. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

workout_place_select()

#At home exercises
atHome_chest_workouts = {
    "Beginner": [
        "Knee Push-Ups",
        "Incline Push-Ups",
        "Standard Push-Ups",
        "Resistance Band Chest Press",
        "Dumbbell Chest Press",
        "Wall Push-Ups",
        "Chest Dips on a Chair",
        "Resistance Band Pull Apart",
        "Floor Press with Dumbbells",
        "Incline Chest Press with Dumbbells",
        "Resistance Band Chest Fly",
        "Floor Fly with Dumbbells"
    ],
    "Intermediate": [
        "Standard Push-Ups",
        "Wide Grip Push-Ups",
        "Narrow Push-Ups",
        "Resistance Band Chest Fly",
        "Dumbbell Chest Fly",
        "Decline Push-Ups",
        "Plyometric Push-Ups",
        "Staggered Push-Ups",
        "Archer Push-Ups",
        "Dumbbell Pullover",
        "Resistance Band Incline Press",
        "Resistance Band Decline Press"
    ],
    "Advanced": [
        "Decline Push-Ups",
        "Plyometric (w/ Clap) Push-Ups",
        "Push-Up Hold",
        "Resistance Band Incline Press",
        "Resistance Band Decline Press",
        "Dumbbell Pullover",
        "Incline Dumbbell Chest Press",
        "Decline Dumbbell Chest Press",
        "Incline Dumbbell Fly",
        "Decline Dumbbell Fly",
        "Single-Arm Dumbbell Chest Press",
        "Spiderman Push-Ups"
    ],
}

atHome_back_workouts = {
    "Beginner": [
        "Superman Exercise",
        "Resistance Band Rows",
        "Bent-Over Dumbbell Rows",
        "Dumbbell Deadlift",
        "Single-Arm Dumbbell Row",
        "Resistance Band Pulldowns",
        "Resistance Band Face Pulls",
        "Cat-Cow Stretch",
        "Bird-Dog Exercise",
        "Wall Angels",
        "Prone T Extension",
        "Seated Resistance Band Row"
    ],
    "Intermediate": [
        "Bent-Over Dumbbell Rows",
        "T-Bar Rows (using resistance band or dumbbells)",
        "Renegade Rows",
        "Dumbbell Deadlift",
        "Reverse Fly",
        "Resistance Band Pull Aparts",
        "Resistance Band Lat Pulldowns",
        "Single-Leg Deadlift",
        "Dumbbell Shrugs",
        "Resistance Band High Rows",
        "Chest Supported Dumbbell Row",
        "Inverted Rows (use sturdy table)"
    ],
    "Advanced": [
        "Pull-Ups or Assisted Pull-Ups",
        "Chin-Ups or Assisted Chin-Ups",
        "Single-Arm Rows",
        "Renegade Rows",
        "Dumbbell Deadlift",
        "T-Bar Rows",
        "Chest Supported Dumbbell Rows",
        "Reverse Fly",
        "Resistance Band Pull Aparts",
        "Archer Rows (w/ resistance band)",
        "Resistance Band Straight-Arm Pulldown"
    ],
}

atHome_core_workouts = {
    "Beginner": [
        "Plank",
        "Knee Tucks",
        "Bird-Dog",
        "Dead Bug",
        "Heel Taps",
        "Mountain Climbers",
        "Leg Raises",
        "Flutter Kicks",
        "Bicycle Crunches",
        "Standing Side Crunches",
        "Side Plank",
        "Russian Twist"
    ],
    "Intermediate": [
        "V-Ups",
        "Plank with Shoulder Tap",
        "Toe Touches",
        "Reverse Crunches",
        "Hanging Leg Raises (use sturdy bar)",
        "Side Plank with Leg Lift",
        "Plank Jacks",
        "Windshield Wipers",
        "Seated Leg Lifts",
        "Rolling Plank",
        "Commandos",
        "Jackknife Sit-Ups"
    ],
    "Advanced": [
        "Dragon Flags",
        "L-Sit",
        "Hollow Body Hold",
        "Bicycle Planks",
        "Plank to Pike",
        "Hanging Leg Raises (Straight Legs)",
        "Side Plank with Hip Dips",
        "Star Plank",
        "Oblique V-Ups",
        "Advanced Russian Twists",
        "Around the World Planks"
    ],
}
atHome_shoulder_workouts = {
    "Beginner": [
        "Arm Circles",
        "Front Raises",
        "Lateral Raises",
        "Shoulder Taps",
        "Wall Push-Ups",
        "Pike Push-Ups",
        "Seated Dumbbell Press",
        "Resistance Band Front Raise",
        "Resistance Band Lateral Raise",
        "Reverse Fly",
        "Overhead Press",
        "Scapular Wall Slides",
        ],
    "Intermediate": [
        "Handstand hold Against Wall",
        "Push-Up to Shoulder Tap",
        "Arnold Press",
        "Upright Rows",
        "Standing Dumbbell Press",
        "Resistance Band Shoulder Press",
        "Front Plank to Pike",
        "Renegade Rows",
        "Around the World",
        "Dumbbell Shrugs",
        "Y Raises",
        "Resistance Band Pul Apart",
        ],
    "Advanced": [
        "Handstand Push-Ups",
        "Lateral Raise to Front Raise",
        "Pike Push-Ups (Feet Elevated)",
        "Single-Arm Dumbbell Press",
        "Bent-Over Lateral Raise",
        "Standing Arnold Press",
        "Handstand Walks",
        "Decline Push-Ups",
        "Face Pulls",
        "Single-Arm Plank",
        "Resistance Band High Pulls",
        "T Push-Ups",
        ],
    },

atHome_arms_workouts = {
    "Beginner": [
        "Bicep Curls",
        "Tricep Dips (Sturdy Chair)",
        "OVearhed Tricep Extension",
        "Hammer Curls",
        "Push-Ups",
        "Resistance Band Bicep Curls",
        "Resistance Band Tricep Extension",
        "Isometric Bicep Hold",
        "Isometric Tricep Hold",
        "Dumbbell Punches",
        "Wrist Curls",
        "Reverse Wrist Curls",
    ],
    "Intermediate": [
        "Chin-Ups",
        "Diamond Push-Ups",
        "Concentration Curls",
        "Skull Crushers",
        "Resistance Band Hammer Curls",
        "Resistance Band Tricep Kickbacks",
        "Zottman Curls",
        "Overhead Dumbbell Press",
        "Incline Push-Ups",
        "Spider Curls",
        "Resistance Band Reverse Curls",
        "Close-Grip Push-Ups",
    ],
    "Advanced": [
        "Pull-Ups",
        "One-Arm Push-Ups",
        "Weighted Dips",
        "Drag Curls",
        "One-Arm Tricep Push-Ups",
        "21s Bicep Curls",
        "Weighted Skull Crushers",
        "Resistance Band 21s",
        "Close-Grip Pull-Ups",
        "Towel Curls",
        "Bodyweight Tricep Extensions",
        "Plank to Push-Up",
    ],

}

atHome_legs_workouts = {
    "Beginner": [
        "Bodyweight Squats"
        "Lunges",
        "Glute Bridges",
        "Step-Ups",
        "Side Leg Raises",
        "Wall Sit",
        "Donkey Kicks",
        "Fire Hydrants",
        "Standing Leg Circles",
        "Standing Side Kicks",
        "Marching in Place",
    ],
    "Intermediate": [
        "Bulgarian Split Squats",
        "Single-Leg Deadlifts",
        "Jump Squats",
        "Curtsy Lunges",
        "Pistol Squats (Assisted)",
        "Reverse Lunges",
        "Lateral Lunges",
        "Bridge Marches",
        "Box Jumps",
        "Resistance Band Squats",
        "Standing Calf Riases (Single-Leg)",
        "Chair Step-Ups (Weighted)",
    ],
    "Advanced": [
        "Pistol Squats",
        "Jump Lunges",
        "Box Jumps (Higher)",
        "Single-leg Glute Bridges",
        "Resistance Band Monster Walks",
        "Bulgaria Split Squats (Weighted)",
        "Single-Leg Deadlifts (Weighted)",
        "Wall Sit (Weighted)",
        "Broad Jumps",
        "Tuck Jumps",
        "Lateral Box Jumps",
        "Lateral Lunge (Weighted)",
    ],
}

#At Gym Workouts
atGym_chest_workouts = {
    "",
}

atGym_back_workouts = {
    "",
}

def workout_randomize_select():
    while True:
        print()

workout_randomize_select()