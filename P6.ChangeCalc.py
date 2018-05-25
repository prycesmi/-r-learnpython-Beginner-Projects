"""
NOTE: The specs for this project were found on /r/learnpython.

GOAL: Imagine that your friend is a cashier, but has a hard time counting
back change to customers. Create a program that allows him to input a certain
amount of change, and then print how how many quarters, dimes, nickels, and
pennies are needed to make up the amount needed.

For example, if he inputs 1.47, the program will tell that he needs 5 quarters,
2 dimes, 0 nickels, and 2 pennies.

SUBGOALS:

(1) So your friend doesn't have to calculate how much change is needed, allow
him to type in the amount of money given to him and the price of the item. The
program should then tell him the amount of each coin he needs like usual.

(2) To make the program even easier to use, loop the program back to the top so
your friend can continue to use the program without having to close and open it
every time he needs to count change.
"""

change_dict = {
    'dollar' : 0,
    'quarter' : 0,
    'dime' : 0,
    'nickel' : 0,
    'penny' : 0
}

def calculator(change):
    while change > 0:
        if change >= 100:
            change -= 100
            change_dict['dollar'] += 1
        elif change >= 25:
            change -= 25
            change_dict['quarter'] += 1
        elif change < 25 and change >= 10:
            change -= 10
            change_dict['dime'] += 1
        elif change < 10 and change >= 5:
            change -= 5
            change_dict['nickel'] += 1
        elif change < 5 and change >= 1:
            change -= 1
            change_dict['penny'] += 1
    print "You need the following: "
    for key, value in change_dict.items():
        print("{}: {}".format(key, value)) # Better formats printed dictionary.

    run() # Loops to allow user to input new value.

def run():
    price = float(raw_input("Please enter price of item: "))
    money = float(raw_input("Please enter amount of money given by customer: "))
    change = int(money * 100) - int(price * 100) # Converts base unit to cent to avoid floating arithmetic error.
    calculator(change)

run()
