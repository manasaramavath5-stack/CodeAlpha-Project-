import random

words = ["python", "computer", "programming", "student", "project"]

word = random.choice(words)

guessed_word = ["_"] * len(word)
guessed_letters = []

attempts = 6

print("================================")
print("       WELCOME TO HANGMAN")
print("================================")

while attempts > 0 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Incorrect attempts left:", attempts)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong guess!")
        attempts -= 1

if "_" not in guessed_word:
    print("\nCongratulations!")
    print("You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The correct word was:", word)

print("\nThank you for playing!")