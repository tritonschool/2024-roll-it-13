import random

def roll_die():
    results = random.randint(1,6)
    return results

for item in range (0,10):
    user_score = 0
    double_score = "no"

    roll_1 = roll_die()
    roll_2 = roll_die()

    if roll_1 == roll_2:
        double_score = "yes"

    user_points = roll_1 + roll_2

    print(f"Die 1: {roll_1} \t Die 2 : {roll_2} \t Points: {user_points}")
    print(f"Double score opportunity: {double_score}")


