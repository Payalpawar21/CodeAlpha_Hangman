# Hangman Game

## CodeAlpha Python Programming Internship — Task 1

A simple text-based Hangman game developed using Python. The player guesses a randomly selected word one letter at a time.

## Features

* Uses 5 predefined words
* Randomly selects a word for each game
* Allows the player to guess one letter at a time
* Maximum 6 incorrect guesses
* Displays correctly guessed letters
* Tracks previously guessed letters
* Prevents duplicate letter guesses
* Displays a winning message when the word is guessed
* Displays a game-over message when all incorrect guesses are used
* Runs completely in the console

## Technologies Used

* Python
* Random module
* Lists
* Strings
* While loop
* If-else statements
* User input

## How to Run

1. Make sure Python is installed on your computer.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Navigate to the `Task1_Hangman` folder.
5. Run the following command:

python hangman.py


## Project Structure

Task1_Hangman/
│
├── hangman.py
└── README.md


## How the Game Works

1. The program contains 5 predefined words.
2. One word is selected randomly.
3. The selected word is displayed as underscores.
4. The player enters one letter at a time.
5. If the letter is correct, it is displayed in the correct position.
6. If the letter is incorrect, the incorrect guess count increases.
7. The player can make up to 6 incorrect guesses.
8. The game ends when the player guesses the complete word or reaches 6 incorrect guesses.

## Sample Output

Welcome to Hangman!
Guess the word one letter at a time.
You have 6 incorrect guesses.

Word: _ _ _ _ _ _ _ _ _
Guessed letters:
Incorrect guesses: 0 / 6
Guess a letter: p

Correct guess!

Congratulations! You guessed the word!
The word was: developer


## Internship Task

This project is completed as part of the CodeAlpha Python Programming Internship.

**Task:** Task 1 — Hangman Game
