import random

def roll_die():
    roll_result = random.randint(1,6)
    return roll_result

def two_rolls(who):
    double_score = "no"

    roll_1 = roll_die()
    roll_2 = roll_die()

    if roll_1 == roll_2:
        double_score = "yes"

    user_points = roll_1 + roll_2

    print(f"{who}: {roll_1} & {roll_2} - Total: {user_points}")

    return user_points, double_score

def int_check(question):




    while True:
        error = "Please enter a number that is 13 or more."

        try:
            response = int(input(question))

            if response < 13:
                print(error)
            else:
                return response


        except ValueError:
            print(error)


user_score = 0
robot_score = 0
num_rounds = 0

target_score = int_check("Enter a target score: ")
print(target_score)

while user_score < target_score and robot_score < target_score:
    num_rounds += 1
    print(f"Round {num_rounds}")
    add_points = int(input("How many points have been won?"))
    user_score += add_points

print()
print(f"Your final score is {user_score}")