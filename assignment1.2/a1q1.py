'''
Yuheng Cheng
COMP 1405
Teacher: Professor Hillen
Date: October 04, 2020
Program overview: Prompts the use to declare the upper range of the number to be generated to be guessed,
then a number between 0 and said number is generated and the user is then given 5 guesses to guess it and feedback is given based on their guess

'''
#import the randrange function from random
from random import randrange

#define the function which will find the difference and calculate percentage difference and returns the feedback for user
def difference_calculator(actual_value,guess):
    #calculate the difference
    difference = abs(actual_value - guess)
    #calculate percentage difference
    percentage_difference = (difference/actual_value)*100
    #based on the % difference and the guess output feed back
    if percentage_difference > 50 and guess < actual_value:
        print("WAY TOO LOW!")
    elif percentage_difference > 50 and guess > actual_value:
        print("WAY TOO HIGH!")
    elif 10 <= percentage_difference <= 50 and guess < actual_value:
        print("Too Low")
    elif 10 <= percentage_difference <= 50 and guess > actual_value:
        print("Too High")
    elif 10 > percentage_difference and guess < actual_value:
        print("Slightly Low!")
    elif 10 > percentage_difference and guess > actual_value:
        print("Slightly High")
        #user wins
    else:
        print("Correct!")
        print("Thank your for Playing!")
        quit()
    
#declare a variable for the check that the range onput is valid
range_check = True
while range_check:
    #try to prevent ValueError
    try:
        #ask user for input
        x_max = int(input("Enter the greatest possible positive integer value greater than 0 that can be generated for you to guess\n> "))
        #if the user follows parameters continues
        if x_max > 0:
            x = randrange(1,x_max)
            range_check = False
        #user input negative value
        else:
            print("Please enter a number greater than 0")
    #user inputted value type other than a positive integer
    except ValueError:
        print("Please Enter a positive integer greater than 0")

#loop for 5 guesses
for i in range(5):
    #declare a variable for the loop check to check that guess is valid
    entry_check = True
    #guess counter
    print("You are currently on guess #"+str(i+1))
    #loop to ensure that the input is valid
    while entry_check:
        #try to prevent ValueError
        try:
            #get user input
             user_guess = int(input('Please enter an integer guess\n> '))
             #call the difference calculator function
             difference_calculator(x,user_guess)
             #break the loop
             entry_check = False
        #user entered the wrong data type
        except ValueError:
            print("Please enter an integer")
#user did not guess the number
print("You Lose Good try, the number was",str(x))
print("Thank your for Playing!")
#quit program
quit()