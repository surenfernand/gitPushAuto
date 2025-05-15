import os
import random
from datetime import datetime

def generate_guess_game_code():
    min_val = random.randint(1, 10)
    max_val = random.randint(50, 200)
    messages = ["Try again!", "Nope!", "Keep guessing!", "You can do it!", "Almost there!"]

    code = f'''import random

number_to_guess = random.randint({min_val}, {max_val})
attempts = 0

print("🎯 Welcome to 'Guess the Number'!")
print("I'm thinking of a number between {min_val} and {max_val}.")

while True:
    try:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("{random.choice(messages)} Too low!")
        elif guess > number_to_guess:
            print("{random.choice(messages)} Too high!")
        else:
            print(f"🎉 You guessed it in {{attempts}} attempts!")
            break
    except ValueError:
        print("Please enter a valid number.")
'''

    return code

def save_daily_code():
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"guess_game_{today}.py"
    folder = "daily_guess_game_codes"
    os.makedirs(folder, exist_ok=True)

    with open(os.path.join(folder, filename), "w") as f:
        f.write(generate_guess_game_code())
    
    print(f"✅ Code for {today} saved as {filename}.")

if __name__ == "__main__":
    save_daily_code()
