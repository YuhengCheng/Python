print("HELLO, GAMER! Welcome to the Raven Runner Loot Box Purchasing System.")
choice_check = True
user_name = input("First, what's your player name? ")

print("Please select a loot box from the menu below:")
while choice_check:
    print("\t1. [Common]\tThe GeeGee (1.50)\n\t2. [Rare]\tThe Raven (3.00)\n\t3. [Epic]\tThe Three-Eyed Raven (7.99)")
    box_choice = input(">")
    if box_choice == '1' or box_choice == '2' or box_choice == '3':
        choice_check = False

    else:
        print("Error: That was not a valid selection. Please enter a number between 1-3")
reciept_check = True
while reciept_check:
    if box_choice == '1':
        try:
            quantity = int(input('How many GeeGees ($1.50) would you like to purchase? '))
            if quantity >= 0:
                price = quantity * 1.50
                print("Thanks,{}! Here is your receipt:\n---------------------------------\n{}x GeeGees ($1.50)".format(user_name,quantity))
                print("---------------------------------\nTotal Cost: ${total:.2f}".format(total = price))
                reciept_check = False
                
            elif quantity < 0:
                print("Error: Please enter an integer value 0 or greater")
        except(ValueError):
            print("Error: Please enter an integer value 0 or greater")

    elif box_choice == '2':
        try:
            quantity = int(input('How many Ravens ($3.00) would you like to purchase? '))
            if quantity >= 0:
                price = quantity * 3.00
                print("Thanks,{}! Here is your receipt:\n---------------------------------\n{}x Ravens ($3.00)".format(user_name,quantity))
                print("---------------------------------\nTotal Cost: ${total:.2f}".format(total = price))
                reciept_check = False
            elif quantity < 0:
                print("Error: Please enter an integer value 0 or greater")
        except(ValueError):
            print("Error: Please enter an integer value 0 or greater")
    elif box_choice == '3':
        try:
            quantity = int(input('How many Three-Eyed Ravens ($7.99) would you like to purchase? '))
            if quantity >= 0:
                price = quantity * 7.99
                print("Thanks,{}! Here is your receipt:\n---------------------------------\n{}x Three-Eyed Ravens ($7.99)".format(user_name,quantity))
                print("---------------------------------\nTotal Cost: ${total:.2f}".format(total = price))
                reciept_check = False
            elif quantity < 0:
                print("Error: Please enter an integer value 0 or greater")
        except(ValueError):
            print("Error: Please enter an integer value 0 or greater")

