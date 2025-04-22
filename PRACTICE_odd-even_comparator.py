repeat = "y"
while repeat == "y":
    number = input("Please type a whole number: ")
    
    if not number.isdigit():
        print("Appologies, but "+str(number)+" is not a valid input")
        continue
    number= int(number)
    if number% 2 == 0:
        print("The number " + str(number) + " is even")
    else:
        print("The number " + str(number) + " is odd")
    while True:
        repeat = input("Try again? (y/n): ").lower()
        if repeat not in ("y", "n"):
            print("That's not a valid imput, please type only y or n")
            continue
        else: break
print("Good bye!")
#commit testing
