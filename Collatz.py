# Fun little script for playing around with the Collatz Conjecture.
# Run the script using F5, or go to the "Run" option up on the Menubar

# Python has several "modules" that you can use to add more functionality to your script
import time

# Best practice in python is to define your functions at the TOP of a script.
def CollatzRules( n ):
    # This function follows the rules of the Collatz Conjecture
    if n % 2 == 0:  # This sees if the number is even
        N = int(n/2)
    else:   # This is what happens if n is not even
        N = (3*n)+1

    # This is basically saying "here's what comes out of the function
    return N

def Intro():
    # This is just typing out everything I want to say, with some brief pauses
    # It doesn't actually return any output
    print('Take a number number "n", and apply these rules to get a new number "N".')
    print('')
    print('1) If n is odd, N = (3*n)+1')
    print('')
    print('2) If n is even N = n/2')
    print('')
    time.sleep(10)
    print('If you keep repeating this over and over:')
    print(' n')
    print(' |')
    print('\|/')
    print(' N')
    print('You will eventually get to the number 1 and keep looping forever.')
    time.sleep(5)
    print(' 8')
    print(' |')
    print('\|/')
    print(' 4')
    time.sleep(3)
    print(' |')
    print('\|/')
    print(' 2')
    time.sleep(3)
    print(' |')
    print('\|/')
    print(' 1')
    time.sleep(3)
    print(' |')
    print('\|/')
    print(' 4')
    time.sleep(3)
    print(' |')
    print('\|/')
    print(' 2')
    time.sleep(3)
    print(' |')
    print('\|/')
    print(' 1')
    time.sleep(3)
    print('')
    print('The Collatz Conjecture is that this works for ANY number!')
    print("But nobody has ever been able to prove it, or find a number that doesn't work")
    print('So go ahead, try it!')

def Chain():
    # This is the function that actually performs the Collatz chain operations

    # This is asking you what number you want to use, and saving it as an integer
    CurrentNum = int(input('Type in the number you want to try: '))
    Steps = 0

    # This is keeping the rules going until you enter the infinite loop
    while CurrentNum != 1:
        # Printing the most recent number
        print(' '+str(CurrentNum))
        time.sleep(1)

        # Printing the arrow
        print(' |')
        print('\|/')

        # This is finding a new number based on the standard rules
        NewNum = CollatzRules(CurrentNum)

        # Then saving the new number as the old one
        CurrentNum = NewNum

        # And incrementing the step counter
        Steps += 1

    # The final number of the chain
    print(' 1')
    print('')
    print('The number you chose took '+str(Steps)+' steps to get to the number 1.')

def Menu():
    # This is the script that prints out all the menu options
    # It also tells the main script what your choice is
    print('')
    print('MENU:')
    print('C: Collatz Chain')
    print('I: Introduction')
    print('M: Menu')
    print('Q: Quit')
    print('')
    Choice = input('What do you want to do?: ')
    return Choice

# From here on is the "MAIN" function.
# Basically, this is what happens right when you start the script.
# From here, if it needs to call one of the user-defined functions, it will
Power = 1
Choice = 'I'

# Power button is on
while Power == 1:

    if Choice is 'C':
        Chain()
        Choice = 'M'
    elif Choice is 'I':
        Intro()
        Choice = 'M'
    elif Choice is 'M':
        Choice = Menu()
    elif Choice is 'Q':
        Power = 0
    else:
        print("Sorry? That wasn't one of the options.")
        Choice = 'M'
