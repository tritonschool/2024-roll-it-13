 # Function to check if user enters yes or no
def yes_no(question):
    # Loop until user provides a valid response
    while True:
        # Ask user for input
        response = input(question).lower()

        # Check if response is yes or no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            # Prompt user to enter yes or no if invalid response is given
            print("Please enter yes or no")


def instruction():
    print('''
    
**** Instructions ****
    
Goal: Be the first to reach a specified score (e.g., 50 points).
Round Setup:
Both player and computer roll two dice.
Start with the total shown by the dice as initial points.
Turns:
Player and computer alternate rolling a single die and adding the result to their points.
Aim to get as close to 13 points without going over.
Round Outcomes:
Going over 13 means losing the round (zero points).
If the computer goes over 13, the player wins the round.
If the player gets more points than the computer (but less than 14), they win the round.
Special Cases:
Player's first roll is doubled if it's a double.
Computer's first roll doesn't double if it's a double.
Winning:
The first to reach the specified target score wins the game.
   
   ''')

# Main routine
print()
print("🎲🎲 Roll it 13 🎲🎲")
print()


# Ask user if they want instructions
want_instructions = yes_no("Do you want instructions? ")
print()

# If user wants instructions, print them
if want_instructions == "yes":
    instruction()

# Indicate the program is continuing
print('Program')
