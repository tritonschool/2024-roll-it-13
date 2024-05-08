
while True:

    error = "Please enter a number that is 13 or more."
    try:
        my_num = int(input("Enter an number: "))

        if my_num < 13:
            print(error)
        else:
            print("Your number is ", my_num)


    except ValueError:
        print(error)
