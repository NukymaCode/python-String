def inputInteger():
    inputNumberIsInt = False
    while inputNumberIsInt == False:
        try:  # try to convert user input into an integer number
            number = int(input("Enter an integer number: "))
            inputNumberIsInt = True
            return number
        except ValueError:  # if it gives a ValueError, return to line 2!
            print("Please, introduce an integer number")