secret_number = 7

while True:
    guess = int(input("Guess your number :"))

    if guess < secret_number:
        print(f"Guess a larger number!")
    elif guess > secret_number:
        print(f"Guess a smaller number!")
    else:
        print(f"Well done! You guessed correctly!")
        break
