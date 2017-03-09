# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/
from random import sample
from time import sleep

def welcome_greeting():
    ''' Welcomes the player to the game and gives credit'''
    print("Fill in the Blanks Quiz: Python Programming")
    sleep(3)
    print('''(Credit to Tutorialspoint.com for content
    "https://www.tutorialspoint.com/python/python_variable_types.htm")''')
    print("")
    sleep(3)


def choose_mode():
    '''Player chooses difficulty level'''
    modes = ["easy", "intermediate", "hard"]
    mode_choice = ""
    while mode_choice == "":
        user_input = input("Choose your difficulty level: Easy, Intermediate or Hard: ")
        user_input = str.lower(user_input) # make the answer lower-case
        if user_input in modes:
            mode_choice += user_input
        else:
            print ("I didn't get that, please choose again")
    return mode_choice


def choose_attempts():
    '''Player chooses number of attempts they receive before game moves on
    to the next step'''
    max_attempts = 0
    while max_attempts == 0:
        user_input =  int(input("Please choose number of attempts: "))
        if user_input in range(1,11):
            max_attempts += user_input
        else:
            print ("Oops, I didn't get that, please choose a number between 1 and 10")
    return max_attempts


def solved_puzzle_printer(level, blank_number, answer):
    '''The current puzzle, blank to be solved and answer are passed in. Returns
    the solved puzzle (for that blank)'''
    print("")
    blank = "__" + str(blank_number) +"__"
    level = level.replace(blank, answer)
    print(level)
    print("")
    return level


def move_to_next_blank(blank_number, level, answer):
    '''Called when the player gets the correct answer or runs out of attempts.
    Passes the current puzzle, blank and answer in to print out the solution,
    then returns the attempts(reset to 1), the next blank to be solved and the
    puzzle(solved to this point)'''
    sleep(2)
    level = solved_puzzle_printer(level, blank_number, answer)
    sleep(2)
    attempt = 1
    blank_number += 1
    return attempt, blank_number, level


def wrong_answer(attempt, max_attempts, mode_choice, answer):
    '''Called when the player gets the wrong answer. Takes in the current
    attempt number, the maximum number of attempts, the difficulty level and
    the answer to the current blank. Returns the attempt number (incremented by one)'''
    if attempt < max_attempts: #If they  player has attempts left, prompt to try again.
        print("oops, try again")
        if mode_choice == "intermediate": #prints out hints if on "intermediate" mode
            if len(answer) > attempt: #prints out one letter of answer per attempt
                print("Hint " + str(attempt) + ": The answer starts with: " + answer[0:attempt])
            else: #if the answer is shorter than the number of attempts, print whole answer
                print("The answer is: " + answer)
        sleep(2)
        print("")
    attempt += 1
    return attempt


def answer_checker(answers, max_attempts, level, mode_choice):
    '''Takes in the current puzzle, the answers, the difficulty level and the
    maximum number of attempts. Compares user input to the answer and increments
    the attempts or moves to the next blank accordingly'''
    attempt = 1
    blank_number = 1
    for answer in answers:
        while attempt <= max_attempts:
            user_input = input("Blank " +  "__" + str(blank_number)
            + "__" + " : Attempt " + str(attempt) + " : Please choose an answer: ")
            user_input = str.lower(user_input)
            if user_input != answer:
                attempt = wrong_answer(attempt, max_attempts, mode_choice, answer)
            else:
                print("You got it right! Good job!")
                attempt , blank_number, level = move_to_next_blank(blank_number, level, answer)
                break
        if attempt > max_attempts:
            print ("Oops, you ran out of attempts, the correct answer was: " + answer)
            attempt , blank_number, level = move_to_next_blank(blank_number, level, answer)


def play_game(mode_choice, answer_key, max_attempts):
    '''prints out the puzzle and checks answers for each level. If on easy
    mode, also prints out possible answers in random order'''
    print("")
    sleep(3)
    for level in answer_key:
        print(level)
        print("")
        sleep(3)
        answers = answer_key[level]["answers"]
        if mode_choice == "easy":
            mixed_answers = sample(answers, len(answers))
            print("")
            print ("Possible Answers: " + ", ".join(mixed_answers))
            print("")
        answer_checker(answers, max_attempts, level, mode_choice)



level_one = '''"Variable Types"
__1__s are nothing but reserved __2__ locations to store __3__s.
This means that when you create a __1__ you reserve some space in __2__.
The equal sign (=) is used to assign __3__s to __1__s. The operand to the
left of the = operator is the __4__ of the __1__ and the operand to the
right of the = operator is the __3__ stored in the __1__.'''

level_two = '''"Standard Data Types"
Python has various standard __1__ types that are used to define
the operations possible on them and the storage method for each of them.
Python has five standard __1__ types: __2__, String, __3__, Tuple, and
Dictionary. Python supports four different __2__ types: int
(signed __4__s), long (long __4__s, they can also be represented
in octal and hexadecimal), __5__ (floating point real values) and
complex (complex numbers)'''

level_three = '''"Strings"
__1__s in Python are identified as a contiguous set of
characters represented in the quotation marks. Python allows for either
pairs of single or __2__ quotes. Subsets of __1__s can be taken using the
__3__ operator ([ ] and [:] ) with indexes starting at 0 in the beginning
of the __1__ and working their way from -1 at the end. The plus (+) sign
is the __1__ concatenation operator and the asterisk (*) is the
__4__ operator'''

level_four = '''"Lists and Tuples"
A list contains items separated by __1__s and enclosed
within square brackets ([]). Their elements and __2__ can be __3__.
All the items belonging to a list can be of __4__ data type. A tuple
consists of a number of values separated by __1__s. Tuples are enclosed in
parentheses ( ( ) ) and cannot be __3__.'''

answer_key = {level_one : {"Level": 1,
            "answers" : ["variable", "memory", "value", "name"]},
            level_two : {"Level": 2,
            "answers" : ["data", "number", "list", "integer", "float"]},
            level_three : {"Level": 3,
            "answers" : ["string", "double", "slice", "repetition"]},
            level_four : {"Level": 4,
            "answers" : ["comma", "size", "changed", "different"]}}

def start_game():
    '''Starts the game'''
    welcome_greeting()
    mode_choice = choose_mode()
    max_attempts = choose_attempts()
    play_game(mode_choice, answer_key, max_attempts)
    print("You've completed the Challenge!!! Thanks for playing!")

start_game()
