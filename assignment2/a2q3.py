#import random module to generate float for box drawing 
import random
#define the main function
def main():
    #keeps track of the user purchases
    purchase_list = [0,0,0]
    #a counter to see if the user has bought anything
    reciept_check = 0
    #introduction line
    print("HELLO, GAMER! Welcome to the Raven Runner Loot Box Purchasing System.")
    #get user name
    user_name = input("First, what's your player name? ")
    #briefs the user to what happens in the menu
    print("Please select a loot box from the menu below:")
    #call the lootbox selection function to update the purchase list with user selections
    purchase_list = lootbox_selection(purchase_list)
    #for loop to see if the list is filled with zeros or not to determine if user is buying anything
    for i in range (len(purchase_list)):
        if purchase_list[i] == 0:
            reciept_check +=1
    #if an element in purchase list is non-zero print reciept
    if reciept_check != 3:
        reciept(user_name,purchase_list)
        box_open(purchase_list)
    #don't print reciept for user if they have not bought anything
    else:
        #thank user
        print("Thank you for visiting our store!")
    #quit
    quit()

#define loot box selection function
def lootbox_selection(pl):
    #variable to loop back to this menu if user does not select option 4
    still_shopping = True
    #keeps user if still shopping
    while still_shopping:
        #variable for while loop to see if user enters a valid value
        choice_check = True
        #loop to check is it is a valid entry
        while choice_check:
            #print choices for user
            print("\t1. [Common]\tThe GeeGee (1.50)\n\t2. [Rare]\tThe Raven (3.00)\n\t3. [Epic]\tThe Three-Eyed Raven (7.99)\n\t4. Complete Purchase")
            #get user input
            box_choice = input(">")
            #check if the input is valid
            if box_choice == '1' or box_choice == '2' or box_choice == '3' or box_choice == '4':
                #breaks loop
                 choice_check = False
            #tells user that is an invalid entry
            else:
                 print("Error: That was not a valid selection. Please enter a number between 1-4")
        #if user selects geegees
        if box_choice == '1':
            #add first value of purchase list to user selection through calling the quantity_selection function
            pl[0] += quantity_selection(box_choice)
        #if user selects ravens
        elif box_choice == '2':
             #add second value of purchase list to user selection through calling the quantity_selection function
            pl[1] += quantity_selection(box_choice)
        #if user selects three eyed raven
        elif box_choice == '3':
            #add third value of purchase list to user selection through calling the quantity_selection function
            pl[2] += quantity_selection(box_choice)
        #if user selects complete purchase
        elif box_choice == '4':
            #return the purchase list to update the main list
            return pl
            
#define quantity_selection
def quantity_selection(choice):
    #variable for while loop to see if user enters valid input
    quantity_check = True
    #lists with items and product pirces to make printing easier
    product_name = ["GeeGee", "Raven", "Three-Eyed Raven"]
    product_price = ("1.50", "3.00", "7.99")
    #loop to check valid inputs
    while quantity_check:
        #try and except to prevent ValueErrors
            try:
                #get user input
                quantity = int(input("How many {0} (${1}) would you like to purchase? ".format(product_name[int(choice)-1],product_price[int(choice)-1])))
                #if user entry is greater than or equal to 0 update the purchase list value in lootbox_selection
                if quantity >= 0:
                    return(quantity)
                #if user entry is less than 0 print error message
                elif quantity < 0:
                    print("Error: Please enter an integer value 0 or greater")
            #except ValueError for when users enter a float or a string
            except(ValueError):
                #print error message
                print("Error: Please enter an integer value 0 or greater")
#define reciept function
def reciept(un,pl):
    #calculate total price
    total_price = pl[0]*1.50 +pl[1]*3.00+pl[2]*7.99
    #print thank you to user and start printing the reciept
    print("Thanks,{}! Here is your receipt:".format(un))
    print("---------------------------------")
    #if user has purchased one or more geegee boxes print on reciept
    if pl[0] > 0:
        print("{0}x\tGeeGees\t($1.50)".format(pl[0]))
    #if user has purchased one or more raven boxes print on reciept
    if pl[1] > 0:
        print("{0}x\tRavens\t($3.00)".format(pl[1]))
    #if user has purchased one or more three eyed raven boxes print on reciept
    if pl[2] > 0:
        print("{0}x\tGeeGees\t($7.99)".format(pl[2]))
    print("---------------------------------")
    #print total price
    print("Total Cost: ${total:.2f}".format(total = total_price))
    print("Good luck, gamer!")

#define class for box for simplicity in box_open function
class box:
    def __init__(self,rarity,common,epic):
        #assign properties
        self.rarity = rarity
        self.common = common
        self.epic = epic
#define box_open
def box_open(pl):
    #create objects for each box with its box type and thresholds for common and rare items
    Geegee = box("common",0.8,0.95)
    Raven = box("rare",0.5,0.9)
    ThreeRaven = box("epic",0.3,0.8)
    #create list full of objects to be able to use for loops
    boxes = [Geegee,Raven,ThreeRaven]
    #tell user what is going on
    print("Time to Open Boxes")
    print("------------------------")
    #for loop to go through each type of box
    for i in range(len(pl)):
        #see if user has purchased any of the box being checked
        if pl[i] > 0:
            #loop to open the quantity of the type of box in question
            for c in range(pl[i]): 
                #inform which box is being opened
                print("Opening {0} box {1}".format(boxes[i].rarity,c+1))
                #generate number
                generated_number = random.random()
                #if generated number is equal or below common threshold print it is a common item
                if generated_number <= boxes[i].common:
                    print("\tIt's a common item!")
                #if generated number is greater common threshold but less than the epic threshold print it is a rare item
                elif boxes[i].common < generated_number < boxes[i].epic:
                    print("\tIt's a rare item!")
                #any other case print it is an epic item
                else:
                    print("\tIt's an EPIC ITEM!!!")


#call main
if __name__ == "__main__":
    main()