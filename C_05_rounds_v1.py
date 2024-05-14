import random

def roll_die():
    results = random.randint(1,6)
    return results

def two_rolls():
    double_score = "no"

    roll_1 = roll_die()
    roll_2 = roll_die()

    if roll_1 == roll_2:
        double_score = "yes"

    user_points = roll_1 + roll_2

    print(f"Die 1: {roll_1} \t Die 2 : {roll_2} ")


    return user_points, double_score


print("Press <enter> to begin this round: ")
input()

user_first = two_rolls()
user_points = user_first[0]
double_points = user_first [1]

if double_points == "no":
    double_feedback = ""
else:
    double_feedback = "If you win this round, you gain double points!"

print(f"You rolled a total of {user_points}.  {double_feedback}")
print()

computer_first = two_rolls()
computer_points = computer_first[0]

print(f"The robot rolled a total of {computer_points}.")


while computer_points <= 13 and user_points <= 13:
    print()
    roll_again = input("Do you want to roll the dice (type 'no' to pass and 'yes' to play): ")
    if roll_again == "yes":
        user_move = roll_die()
        user_points += user_move
        print(f"You rolled a {user_move}.  You now have {user_points} points.")

    print("\nTo contine press <enter>")
    input()

    computer_move = roll_die()
    computer_points += computer_move
    print(f"The robot rolled a {computer_move}. The robot" 
          f" now has {computer_points}.")

    print()
    if user_points > computer_points:
        result = "You are ahead."
    else:
        result = "The robot is ahead."

    print(f"***Round Update***: {result} ")
    print(f"User Score: {user_points} \t | \t Robot Score: {computer_points}")


if user_points < computer_points:
    print("You suck cause you lost"
          " no points for you"
          f" the robot has {computer_points} more points.")

else:
    print("You Won"
          f"{user_points} has been added to you")