import random
words = ['chicken', 'dog', 'cat', 'mouse', 'frog']
lives_remaining = 14


def play():
    word = pick_a_word()
    while True:
        guess = get_guess(word)
        if process_guess(guess, word):
            print('You Win! Jolly good')
            break
        if lives_remaining == 0:
            print('You are Hanged')
            print('The word was: ' + word)
            break


def pick_a_word():
    return random.choice(words)


def get_guess(word):
    print_word_with_blanks(word)
    print('Live remaining: ' + str(lives_remaining))
    guess = input(' Guess a letter or whole word?')
    return guess


def print_word_with_blanks(word):
    print('print_word_with_blanks:not done yet')


def process_guess(guess, word):
    global lives_remaining
    lives_remaining = lives_remaining - 1
    return False

play()