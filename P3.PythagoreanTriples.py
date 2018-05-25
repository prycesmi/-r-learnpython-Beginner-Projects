"""
NOTE: The specs for this project were found on /r/learnpython.

MAIN GOAL

Create a program that allows the user to input the sides of any triangle, and
then return whether the triangle is a Pythagorean Triple or not.

SUBGOALS

(1) If your program requires users to input the sides in a specific order,
change the coding so the user can type in the sides in any order. Remember, the
hypotenuse (c) is always the longest side.

(2) Loop the program so the user can use it more than once without having to
restart the program.
"""



def game():
    dimensions = []

    # Adds integers to dimensions of triangle list.
    dimensions.append(int(raw_input('Please enter the length of side 1: ')))
    dimensions.append(int(raw_input('Please enter the length of side 2: ')))
    dimensions.append(int(raw_input('Please enter the length of side 3: ')))

    dimensions.sort() # Orders the dimensions into ascending order.

    if dimensions[2] ** 2 == (dimensions[0] ** 2 + dimensions[1] ** 2):
        print "Yes, this is a Pythagorean Triple!"
    else:
        print "This is just a normal triangle!"

    game()

game()
