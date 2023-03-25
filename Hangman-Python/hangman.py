from random import choice, random

dictionary_file = "dictionary.txt"


# make a dictionary from a dictionary file ('dictionary.txt', see above)
# dictionary keys are word sizes (1, 2, 3, 4, …, 12), and values are lists of words
# for example, dictionary = { 2 : ['Ms', 'ad'], 3 : ['cat', 'dog', 'sun'] }


def import_dictionary(filename):
dictionary = {}
max_size = 12
    try:
        with open(filename, 'r') as file:
            for line in file:
                word = line.strip()
                size = len(word)
                if size > max_size:
                    size = max_size
                if size not in dictionary:
                    dictionary[size] = []
                dictionary[size].append(word)
    except Exception as e:
           print(f"Error: {e}")
    return dictionary

# print the dictionary (use only for debugging)
def print_dictionary(dictionary):
    for key in range(1, 13):
        if key in dictionary:
            print(f"{key}: {dictionary[key]}")



# get options size and lives from the user, use try-except statements for wrong input
def get_game_options () :
    try:
        size = int(input("Please choose a size of a word to be guessed [3-12, default any size]: ") or 0)
        lives = int(input("Please choose a number of lives [1-10, default is 5]: ") or 5)
    except ValueError:
        print("Invalid input. Using default values.")
        size = 0
        lives = 5
    return (size, lives)


def play_game(dictionary, size, lives):
    if size == 0:
        size = choice(list(dictionary.keys()))
    word = choice(dictionary[size])
    hidden_word = ['_' for _ in word]
    chosen_letters = set()

    while lives > 0 and '_' in hidden_word:
        print(f"Letters chosen: {', '.join(sorted(chosen_letters))}")
        print(f"{' '.join(hidden_word)}    lives: {lives} {'X' * lives + 'O' * (5 - lives)}")
        guess = input("Guess a letter: ").lower()

        if guess in chosen_letters:
            print("You already guessed this letter.")
        elif guess in word:
            chosen_letters.add(guess)
            for i, letter in enumerate(word):
                if letter == guess:
                    hidden_word[i] = letter
        else:
            chosen_letters.add(guess)
            lives -= 1
            print("Incorrect!")

    if lives > 0:
        print(f"Congratulations, you guessed the word: {word}")
    else:
        print(f"Sorry, you lost. The word was: {word}")

if __name__ == '__main__' :

    dictionary = import_dictionary(dictionary_file)
    print("Welcome to the Hangman Game! \nPlease choose a size of a word to be guess[ 3 – 12, default any size]:")
    print ("The word size is set to", int(input()), ".")
    print ("Please choose a number of lives [1-10, default is 5]:")
    print ("you have", int(input()), "lives.")
    print_dictionary(dictionary)
    while True:
        size, lives = get_game_options()
        play_game(dictionary, size, lives)
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thanks for playing!")
