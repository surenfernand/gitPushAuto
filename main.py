import random

number_to_guess = random.randint(1, 100)
attempts = 0

print("🎯 Welcome to 'Guess the Number'!")
print("I'm thinking of a number between 1 and 100.")

while True:
    try:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low!!!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"🎉 You guessed it in {attempts} attempts!")
            break
    except ValueError:
        print("Please enter a valid number.")
        
    except KeyboardInterrupt:
