"""
NOTE: The specs for this project were found on /r/learnpython.

GOAL: I'm sure you've used a magic 8 ball at one point in your life.
You ask it a question, turn it right side up and it gives an answer by way of a
floating die with responses written on it. You can create one in python.

RULES:

1. Allow the user to enter their question
2. Display an in progress message (i.e. "thinking")
3. Create 20 responses, and show a random response
4. Allow the user to ask another question or quit

"""

import random # Necessary for generation of random response from Magic 8 Ball
import time # Necessary for "thinking" period

""" Array of Magic 8 Ball responses found on /wiki/Magic_8-Ball """
responses = [
    'It is certain.',
    'It is decidedly so.',
    'Without a doubt',
    'Yes, definitely.',
    'You may rely on it.',
    'You can count on it',
    'As I see it, yes.',
    'Most likely.',
    'Outlook good',
    'Yes.',
    'Signs point to yes.',
    'Absolutely.',
    'Reply hazy try again.',
    'Ask again later.',
    'Cannot predict now.',
    'Better not tell you now.',
    'Cannot predict now.',
    'Concentrate and ask again.',
    'Don\'t count on it',
    'My reply is no.',
    'My sources say no.',
    'Outlook not so good.',
    'Very doubtful.',
    'Chances aren\'t good.'
]

def game():
    input = raw_input('Please enter your question: ')
    print 'Hmm... Let me think about that...'
    time.sleep(5)
    print responses[random.randint(0,23)]
    answer = raw_input('Would you like to ask another question? [Y/N]: ')
    if answer != 'Y':
        print 'Thanks for playing!'
        return
    elif answer == 'Y':
        game()

game() # Initiates the game.
