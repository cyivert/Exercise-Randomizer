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

def dyk_difficulty_level():
    while True:
        print("Do know your training difficulty level?")
        dyk_level = input("(Y/N): ")
        if dyk_level == "Y" or dyk_level == "y":
            return dyk_level
        elif dyk_level == "N" or dyk_level == "n":
            print("Would you like to know your training difficulty level?")
            determine_difficulty_level = input("(Y/N): ")
            if determine_difficulty_level == "Y" or determine_difficulty_level == "y":
                def my_difficulty_level():
                    while True:
                        print("We have 3 cateogries of training difficulty level which are:")
                        time.sleep(1)
                        for key, value in difficulty_level.items():
                            print(f"{key}: {value}")
                            time.sleep(1)
                        print()
                        print("Please answer the following questions to determine your training difficulty level: ")
                        print()

                        questions = [
                            ("Q1: Resistance Training Experience",
                            "a. This will be my first experiences with structured resistance training. (1 points)",
                            "b. I have trained consistently for 6 months 2 years. (2 points)",
                            "c. I have trained consistently for more than 2 years. (3 points)",),
                            ("Q2: Recent Training Consistency",
                            "a. I have not trained recently, or it has been more than 3 months since I last trained. (1 point)",
                            "b. I trained 1-2 weeks ago. (2 points)",
                            "c. I currently train 2-4 times per week. (3 points)",),
                            ("Q3: General Daily Activity Level",
                            "a. I am mostly sedentary (e.g., desk job, little physical activity). (1 point)",
                            "b. I am somewhat active (e.g., recreational athlete, regular hikes). (2 points)",
                            "c. I am very active (e.g., daily physical exercise, athletic job). (3 points)"),
                            ("Q4: Athletic Background"
                            "a. I have no athletic background or participation in sports. (1 point)",
                            "b. I played more than one sport in high school. (2 points)"
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
                                answer = input("Your asnwer: ")
                                if answer.lower() not in ['a', 'b', 'c']:
                                    print("Invalid Answer. Please enter either a or b or c")
                                    continue
                                answers.append(answer.lower())
                                break
                            print()

                        score =sum([1 if answer == 'a' else 2 if answer == 'b' else 3 for answer in answers])

                        print(f"Your score is: {score}")
                        if score <= 10:
                            print("Your training difficulty level is Beginner")
                        elif 10 < score <= 14:
                            print("Your training difficulty level is Intermediate")
                        elif score > 14:
                            print("Your training difficulty level is Advanced")

                my_difficulty_level()
                return determine_difficulty_level
            elif determine_difficulty_level == "N" or determine_difficulty_level == "n":
                return dyk_level

dyk_difficulty_level()

# -- After difficulty level is confirmed --
#def difficulty_level_select(difficulty_level):
#    while True:
#        print("Select difficulty level:")
#        for key, value in difficulty_level.items():
#            print(f"{key}: {value}")

#difficulty_level_select(difficulty_level)


