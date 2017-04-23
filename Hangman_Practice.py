##### Psudeo code#####
# 1) generate list of words
# 2) ask user for a letter
# 3) check if letter is in the word
#   3a) if not, reduce lives by 1
#   3b) if it is, add to "guessed" variable and show remaining spaces
# 4) if lives == 0, end game
# 5) if all letters guessed, end game
######################

import random
blanks = ''
lives = 14

# list of words to work with
words_list = ['chicken', 'horse', 'cat', 'mouse', 'dog', 'goat']

# randomly chooses a word from words_list then prints it to stdout
chosen_word = random.choice(words_list)
print('Randomly chosen word:', chosen_word)


guessed_letter = input('Guess a letter: ')  # prompt user to enter a letter
while lives <= 14 and lives > 0:  # continue while there are lives remaining
    for each_letter in chosen_word:  # for each letter (each_letter) in chosen_word run the if statement below
        if guessed_letter == each_letter:  # if the letter the user entered is in chosen_word then print something
            print('You got one right. ', guessed_letter, "is in the word")
        else:  # if the letter the user entered is NOT in chosen_word then decrement lives by 1 and try again
            print('Sorry, ', guessed_letter, 'is not in the word')
            lives = lives - 1
            print('You have', lives, 'lives remaining.')
			#continue
    #break