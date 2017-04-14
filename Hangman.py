#Stopped pg.52
#Start with completing process_guess function
#Added a commend here for fun
#Added yet another fun comment to test using Branches

import random #imports random module
words = ['chicken', 'dog', 'cat', 'mouse', 'frog'] #word list for the game
lives_remaining = 14 #lives for the game
guessed_letters = ''


def play(): #this function controls the game
    word = pick_a_word() #grab a word from the words variable
    while True:
        guess = get_guess(word) #function that gets a guess from the user
        if process_guess(guess, word): #if users guess is the same as what the random module pulled from the words variable then they win
            print('You Win! Jolly good')
            break #end game
        if lives_remaining == 0: #if there are no lives left then you die
            print('You are Hanged')
            print('The word was: ' + word)
            break #end game


def pick_a_word(): #uses the random module to randomly pick a word from the words variable
    return random.choice(words)


def get_guess(word): #get guess from user
    print_word_with_blanks(word)
    print('Live remaining: ' + str(lives_remaining))
    guess = input(' Guess a letter or whole word?')
    return guess


'''checks if the letter the user guessed is in the word variable. If it is then the letter is added to display_word which is then printed.
if the letter is not in the word variable then a hyphen/underscore is added to display_word.'''
def print_word_with_blanks(word):
    display_word = ""
    for letter in word:
        if guessed_letters.find(letter) > -1: #letter found in guessed_letters. the find function returns -1 if it doesn't find anything
            display_word = display_word + letter
        else:
            display_word = display_word + '_' #letter not found in guessed_letters
    print(display_word)


def process_guess(guess, word): #reduces the lives remaining by one for ever wrong guess
    global lives_remaining
    global guessed_letters
    lives_remaining = lives_remaining - 1
    guessed_letters = guessed_letters + guess
    return False

play()