
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

target_score = int_check("Enter a target score: ")
print(target_score)

while user_score < target_score and robot_score < target_score:
    print("Round heading goes here...")
    add_points = int(input("How many points have been won?"))
    user_score += add_points

print()
print(f"Your final score is {user_score}")