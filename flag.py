import random

def guess_numbers():
    print("Think of a list of numbers in your mind, and I'll try to guess them!")
    guessed_numbers = []
    number_count = int(input("How many numbers are you thinking of? "))

    for i in range(number_count):
        guess = random.randint(1, 100)  # Adjust range as needed
        print(f"Is your number {guess}? (yes/no)")
        response = input().strip().lower()
        if response == 'yes':
            guessed_numbers.append(guess)
            print("Got it!")
        else:
            print("Okay, I'll keep trying.")

    print("\nThe numbers I guessed are:")
    print(guessed_numbers)

# Run the guessing game
guess_numbers()
