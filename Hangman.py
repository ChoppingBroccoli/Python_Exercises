'''
Completed code but it's broken. As soon as the first letter in the word is guessed the games
ends as a Win. 
'''


import random  # imports random module
words = ['chicken', 'dog', 'cat', 'mouse', 'frog']  # word list for the game
lives_remaining = 14  # lives for the game
guessed_letters = ''  # initialize the number of letters guessed


def play():  # this function controls the game
    word = pick_a_word()  # grab a word from the words variable
    print(word) # prints the word that was randomly chosen  by the pick_a_word function (for debugging purposes)
    while True:
        guess = get_guess(word)  # function that gets a guess from the user
        if process_guess(guess, word):  #if guess is the same as what the random module pulled from the words variable then they win
            print('You Win! Jolly good. You guessed,', word)
            break  # end game
        if lives_remaining == 0:  # if there are no lives left then you die
            print('You are Hanged')
            print('The word was: ' + word)
            break  # end game


def pick_a_word():  # uses the random module to randomly pick a word from the words variable
    return random.choice(words)


def get_guess(word):  # get guess from user
    print_word_with_blanks(word) # Moved to end of function for testing but it made things worse. App did not register first letter guess.
    print('Lives remaining: ' + str(lives_remaining))
    guess = input('Guess a letter or whole word?')
    return guess


'''
checks if the letter the user guessed is in the word variable. If it is then the letter is added to display_word which is then printed.
if the letter is not in the word variable then a hyphen/underscore is added to display_word.
'''
def print_word_with_blanks(word):
    display_word = ""
    for letter in word:
        if guessed_letters.find(letter) > -1:  # letter found in guessed_letters. the find function returns -1 if it doesn't find anything
            display_word = display_word + letter
        else:
            display_word = display_word + '_'  # letter not found in guessed_letters
    print(display_word)


def process_guess(guess, word):  # Checks if the user has guessed one word of word or the entire word
    if len(guess) > 1:
        return whole_word_guess(guess, word)
    else:
        return single_letter_guess(guess, word)


def single_letter_guess(guess, word):  # determines if a single letter has been guessed.
    global guessed_letters
    global lives_remaining
    if word.find(guess) == -1:
        # word guess was incorrect
        lives_remaining = lives_remaining - 1
    guessed_letters = guessed_letters + guess
    if all_letters_guessed(word):
        return True
    return False


def all_letters_guessed(word):  # determines if all of the letters in the word have been guessed
    for letter in word:
        if guessed_letters.find(letter) == -1:
            return False
        return True


def whole_word_guess(guess, word):  # determines if the whole word was guessed. If not, -1 live
    global lives_remaining
    if guess.lower() == word.lower():
        return True
    else:
        lives_remaining = lives_remaining - 1
        return False


play()