secret = 35

guess = int(input("Guess the secret number (between 0 and 45): "))

if guess == secret:
    print("Congratulations! The secret number is 35.")
else:
    print("Sorry, your guess is not correct. Try again another time.")
