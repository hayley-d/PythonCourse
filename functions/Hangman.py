import random
from hangman_art import stages, logo
import hangman_words

stage = len(stages)


def choose_word():
    random_index = random.randint(0, len(hangman_words.word_list) - 1)
    return hangman_words.word_list[random_index]


def hangman(level):
    if level == len(stages):
        return stages[level - 1]
    return stages[level]


def remove_letter(letter, word):
    modified_word = word.replace(letter, '', 1)
    return modified_word


def add_guess(letter, guessed_letters):
    global original_word
    guessed_letters = [letter if original_word[i] == letter and guessed != letter else guessed for i, guessed in enumerate(guessed_letters)]
    return guessed_letters


# Start the game
print(logo)

# get the random word
word = choose_word()
original_word = word
print(word)

# create an array with empty spaces
guessed_letters = ['_'] * len(word)

while '_' in guessed_letters and stage != 0:
    print(guessed_letters)
    # Get the guessed letter
    input_letter = input("Guess a letter: ")

    # check if the letter is correct
    if input_letter in word:
        # add the letter into the array
        guessed_letters = add_guess(input_letter, guessed_letters)
        word = remove_letter(input_letter, word)

    else:
        stage -= 1
        print(hangman(stage))

if stage == 0:
    print("Game Over")
    print(hangman(stage))
else:
    print("You Won!")
    print(hangman(stage))
