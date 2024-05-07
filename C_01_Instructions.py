print("🎲🎲 Roll it 13 🎲🎲")


#loop for test

while True:
    want_instructions = input("Do you want instructions?").lower()

    if want_instructions == "yes" or want_instructions == "y":
        print("you said yes")

    elif want_instructions == "no" or want_instructions == "n":
        print("you said no")
    else:
        print(" please say yes or no")
