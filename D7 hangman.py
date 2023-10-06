 # not currently working
import random
# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import D7_Hangman_words

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

 
end_of_game = False

# word_list = ["aardvark", "baboon", "camel"]


chosen_word = random.choice(D7_Hangman_words.word_list)
word_length = len(chosen_word)

#set lives to 6
lives = 6

display = []
for letter in chosen_word:
    display += "_"
print(display)

# print(f"word: {word}")
# convert word to list of letters
# print(f'List of Characters ={list(chosen_word)}')
# chosen_word_list ={list(chosen_word)}

# repeat while lives left
while not lives == 0:
# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
  while not end_of_game:
    guess = input("Choose a letter. \n").lower()

#   Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    for position in range(0, word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] =[letter]

    print(display) 
    if guess not in chosen_word:
       lives -= 1
       if lives == 0:
        end_of_game = True
        print("You lose!")

    # check for any remaining blanks
    if "_" not in display:
        end_of_game = True
        print("You win!")
#if lives == 0:
#  print("You lose!")

# print hangman image
    print(stages[lives])
