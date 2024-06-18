# Keep asking the user for input untill they enter a numnber between 1 and 10 





while True:
    number = int (input("Enter a number between 1 to 10 :  "))
    if 1 <= number <= 10:
        print("Thanks")
        break
    else: 
        print("Invalid number, try again")