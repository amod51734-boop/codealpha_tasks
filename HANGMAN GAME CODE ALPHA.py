import random

words = [
    "phoenix",
    "mystery",
    "treasure",
    "adventure",
    "keyboard",
    "notebook",
    "umbrella",
    "elephant",
    "chocolate",
    "mountain"
]

word = random.choice(words)

guessed = ""
chances = 6

print("Welcome to Hangman!")

while chances > 0:

    display = ""

    for letter in word:
        if letter in guessed:
            display = display + letter
        else:
            display = display + "_"

    print(display)

    if display == word:
        print("Congratulations! You WON 🏆")
        break

    guess = input("Enter a letter: ")

    if guess in word:
        guessed = guessed + guess
        print("Correct!")
    else:
        chances = chances - 1
        print("Wrong!")
        print("Chances Left:", chances)

if chances == 0:
    print("You Lost!😞")
    print("The word was:", word)