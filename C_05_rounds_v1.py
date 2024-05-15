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


print("Press <enter> to begin this round: ")
input()

user_first = two_rolls("User")
user_points = user_first[0]
double_points = user_first [1]

if double_points == "yes":
 print("If you win this round, you gain double points!")

#print(f"You rolled a total of {user_points}.  {double_feedback}")
#print()

robot_first = two_rolls("Robot")
robot_points = robot_first[0]

print(f"The robot rolled a total of {robot_points}.")


while robot_points < 13 and user_points < 13:
    print()
    roll_again = input("Do you want to roll the dice (type 'no' to pass and 'yes' to play): ")
    if roll_again == "yes":
        user_move = roll_die()
        user_points += user_move

        if user_points > 13:
            print(f"💥💥💥You suck cause you rolled a {user_move} making your total {user_points} which is over 13 points.💥💥💥")

            user_points = 0

            break

        else:
            print(f"You rolled a {user_move} and have a total of {user_points}.")


    robot_move = roll_die()
    robot_points += robot_move

    if robot_points > 13:
        print(f"💥💥💥The robot rolled a {robot_move} making there total {robot_points} which is over 13 sadly.💥💥💥")
        robot_points = 0
        break

    else:
        print(f"The robot rolled a {robot_move} which makes there total {robot_points}.")


    print()
    if user_points > robot_points:
        result = "You are ahead."
    elif user_points < robot_points:
        result = "The robot is ahead."
    else:
        result = "Its a tie"

    print(f"{result} \tUser: {user_points} \t | \t Robot: {robot_points}")

print()
if user_points < robot_points:
    print(
          " no points for you so"
          f" and the robot has {robot_points} more points.")

else:

    if double_points == "yes":
        user_points *= 2

    print("You Won")
    print()
    print( f" {user_points} has been added to your overall score")

