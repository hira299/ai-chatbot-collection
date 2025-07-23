import random

def get_random_number(start, end):
    """Generate a random number between start and end (inclusive)."""
    return random.randint(start, end)

def get_user_guess():
    """Get the user's guess."""
    guess = input("Enter your guess: ")
    return int(guess)

def check_guess(guess, correct_number):
    """Check the user's guess against the correct number."""
    if guess < correct_number:
        return "Your guess is too low."
    elif guess > correct_number:
        return "Your guess is too high."
    else:
        return "Congratulations! You guessed it!"

def play_game():
    """Main function to play the number guessing game."""
    print("Welcome to the Number Guessing Game!")
    start = 1
    end = 100
    correct_number = get_random_number(start, end)
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        guess = get_user_guess()
        attempts += 1
        result = check_guess(guess, correct_number)
        print(result)
        
        if guess == correct_number:
            print("You win!")
            break
    else:
        print(f"You lose! The correct number was {correct_number}.")

if __name__ == "__main__":
    play_game()
