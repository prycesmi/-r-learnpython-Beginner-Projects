"""
NOTE: The specs for this project were found on /r/learnpython.

When some people receive change after shopping, they put it into a container and
let it add up over time. Once they fill up the container, they'll roll them up
in coin wrappers which can then be traded in at a bank for what they are worth.
While most banks will give away coin wrappers for free, it's convenient to have
an idea of how many you will need. Instead of counting how many coins you have,
it's easier to separate all of your coins, weigh them, and then estimate how
many of each type you have and then how many wrappers you'll need.

For example, if you weigh all of your dimes and see that you have 1276.9g of
them, you can estimate that you have about 563 dimes (since each one is 2.268g)
and you would be able to fill 11 dime wrappers.

GOAL: Create a program that allows the user to input the total weight of each
type of coin they have (pennies, nickels, dimes, and quarters), and then print
out how many of each type of wrapper they would need, how many coins they have,
and the estimated total value of all of their money.

Weight of each coin and how many fit inside each type of wrapper.

SUBGOALS:

(1) Round all numbers printed out to the nearest whole number.

(2) Allow the user to select whether they want to submit the weight in either
grams or pounds.
"""
import math # Necessary to round UP to ensure we have enough wrappers

# Following values are weight of coin roll in grams or pounds
# Masses and number of coins per roll were obtained from /wiki/Coin_wrapper
quarter_roll_g = 226.8
quarter_roll_p = 0.5

dime_roll_g = 113.4
dime_roll_p = 0.25

nickel_roll_g = 200
nickel_roll_p = 0.44

penny_roll_g = 125
penny_roll_p = 0.275

def menu():
    # .lower() allows for better handling of user input.
    coin = raw_input("Which coin are you working with?: ").lower()
    mass_units = raw_input("Would you like to enter the weight in pounds or grams? [lbs/g]: ").lower()
    mass = int(raw_input("Please enter numerical weight of coins: "))
    converter(coin, mass_units, mass)

def converter(coin, mass_units, mass):
    if coin == 'quarter':
        if mass_units == 'lbs':
            # Converstion to int then conversiton to str allows for dropping of 0 after decimal and concatenation of print statement, respectively
            print "You need " + str(int((math.ceil(mass / quarter_roll_p)))) + " wrapper(s)"
        elif mass_units == 'g':
            print "You need " + str(int((math.ceil(mass / quarter_roll_g)))) + " wrapper(s)"
        else:
            print "There was an error in your entry."
            menu()

    elif coin == 'dime':
        if mass_units == 'lbs':
            print "You need " + str(int((math.ceil(mass / dime_roll_p)))) + " wrapper(s)"
        elif mass_units == 'g':
            print "You need " + str(int((math.ceil(mass / dime_roll_g)))) + " wrapper(s)"
        else:
            print "There was an error in your entry."
            menu()

    elif coin == 'nickel':
        if mass_units == 'lbs':
            print "You need " + str(int((math.ceil(mass / nickel_roll_p)))) + " wrapper(s)"
        elif mass_units == 'g':
            print "You need " + str(int((math.ceil(mass / nickel_roll_g)))) + " wrapper(s)"
        else:
            print "There was an error in your entry."
            menu()

    elif coin == 'penny':
        if mass_units == 'lbs':
            print "You need " + str(int((math.ceil(mass / penny_roll_p)))) + " wrapper(s)"
        elif mass_units == 'g':
            print "You need " + str(int((math.ceil(mass / penny_roll_g)))) + " wrapper(s)"
        else:
            print "There was an error in your entry."
            menu()

    else:
        print "There was an error in your entry."
        menu()

menu()
