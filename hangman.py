import random

words = ["python", "developer", "computer", "programming", "software"]

secret_word = random.choice(words)

guessed_letters = []

incorrect_guesses = 0
max_incorrect_guesses = 6

display_word = ["_"] * len(secret_word)

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")
print()

while incorrect_guesses < max_incorrect_guesses and "_" in display_word:

    print("Word:", " ".join(display_word))
    print("Guessed letters:", ", ".join(guessed_letters))
    print("Incorrect guesses:", incorrect_guesses, "/", max_incorrect_guesses)

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        print()
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        print()
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")

        for index in range(len(secret_word)):
            if secret_word[index] == guess:
                display_word[index] = guess

    else:
        print("Wrong guess!")
        incorrect_guesses += 1

    print()


if "_" not in display_word:
    print("Congratulations! You guessed the word!")
    print("The word was:", secret_word)

else:
    print("Game Over!")
    print("You used all 6 incorrect guesses.")
    print("The word was:", secret_word)