"""
NOTE: The specs for this project were found on /r/learnpython.

GOAL: Create a program that prints out every line to the song "99 bottles of
beer on the wall." This should be a pretty simple program, so to make it a bit
harder, here are some rules to follow.

RULES:

1. If you are going to use a list for all of the numbers, do not manually
type them all in. Instead, use a built in function.

2. Besides the phrase "take one down," you may not type in any numbers/names of
numbers directly into your song lyrics.

3. Remember, when you reach 1 bottle left, the word "bottles" becomes singular.

4. Put a blank line between each verse of the song."""

for bottle in range(99,0,-1):
    if bottle > 2:
        print str(bottle) + ' bottles of beer on the wall, ' + str(bottle) + ' bottles of beer,'
        print 'Take one down and pass it around ' + str(bottle - 1) + ' bottles of beer on the wall.'
        print ''
    elif bottle == 2:
        print str(bottle) + ' bottles of beer on the wall, ' + str(bottle) + ' bottles of beer,'
        print 'Take one down and pass it around ' + str(bottle - 1) + ' bottle of beer on the wall.'
        print ''
    else:
        print str(bottle) + ' bottle of beer on the wall, ' + str(bottle) + ' bottle of beer,'
        print 'Take one down and pass it around, ' + str(bottle - 1) + ' bottles of beer on the wall.'
        print ''
        print 'Go to the store and buy some more, 99 bottles of beer on the wall!'
        print ''
