"""
NOTE: The specs for this project were found on /r/learnpython.
      The madlib template was found on redkid.net/madlibs/

GOAL:

Create a Mad Libs style game, where the program asks the user for certain types
of words, and then prints out a story with the words that the user inputted. The
story doesn't have to be too long, but it should have some sort of story line.

Tip - It's easiest to write out a quick story on a piece of paper or a word
document, and then go back through and see which words the user should be able
to change.

SUBGOALS:

(1) If the user has to put in a name, change the first letter to a capital
letter.

Change the word "a" to "an" when the next word in the sentence begins with a
vowel.
"""

def get_adjective():
    adjective = raw_input("Please enter an adjective: ")
    return adjective

def get_celebrity():
    celebrity = raw_input("Please enter a celebrity: ")
    celebrity = celebrity.lower() # Allows for better handling of user input.
    celebrity = celebrity.title() # Capitalizes first letter of first and last name.
    return celebrity

def get_nouns():
    nouns = []
    counter = 0
    while counter < 4:
        nouns.append(raw_input("Please enter a noun: "))
        counter += 1
    return nouns

def get_plural_nouns():
    plural_nouns = []
    counter = 0
    while counter < 4:
        plural_nouns.append(raw_input("Please enter a plural noun: "))
        counter += 1
    return plural_nouns

def get_type_of_liquid():
    liquid = raw_input("Please enter a type of liquid: ")
    return liquid

def get_verbs():
    verbs = []
    counter = 0
    while counter < 3:
        verbs.append(raw_input("Please enter a verb: "))
        counter += 1
    return verbs

celebrity = get_celebrity()
nouns = get_nouns()
plural_nouns = get_plural_nouns()
liquid = get_type_of_liquid()
verbs = get_verbs()
adjective = get_adjective()

def story():
    print "This is the soliloquy from the play \"Hamlet\", written by " + celebrity
    print "In the third act of this " + adjective + " play, Hamlet, who is sometimes"
    print "called \"the melancholy " + nouns[0] + ",\" is suspiscious of his stepfather"
    print "and hires some actors to act out a scene in which a king is killed"
    print "when someone pours " + liquid + " into his " + nouns[1] + ". First,"
    print "however, he declaims: To be or not to be: that is the " + nouns[2] + ":"
    print "Whether 'tis nobler in the mind to suffer the " + plural_nouns[0] + " and"
    print plural_nouns[1] + " of outrageous fortune, or to take arms against a sea of"
    print plural_nouns[2] + ", and by opposing end them. To die: to sleep; no more;"
    print "and by a sleep to say we end the heartache and the thousand natural"
    print plural_nouns[3] + " that flesh is heir to, 'tis a consumation devoutly to"
    print "be wish'd. To die, to " + verbs[0] + "; to " + verbs[1] + "; perchance to"
    print verbs[2] + ": ay, there's the " + nouns[3] + "."

story()
