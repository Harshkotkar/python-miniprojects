import random
import time

def guess_number():
    while True:
        print("\n🎮 Welcome to the Ultimate Guessing Game! 🎯")
        print("Choose the difficulty level:")
        print("1. Easy (Range: 1-10, Unlimited guesses 🥱)")
        print("2. Medium (Range: 1-25, 10 guesses 🤔)")
        print("3. Hard (Range: 1-100, 5 guesses 😥)")
        print("4. Exit the game 🚪")

        while True:
            try:
                difficulty = int(input("Enter the difficulty level (1/2/3/4): "))
                if difficulty in [1, 2, 3, 4]:
                    break
                else:
                    print("Please select a valid option (1/2/3/4).")
            except ValueError:
                print("Please enter a number (1/2/3/4).")

        if difficulty == 4:
            print("Thanks for playing! See you soon.... 👋")
            return

        # Set difficulty parameters
        if difficulty == 1:
            max_num = 10
            max_attempts = float('inf')  # Unlimited attempts
            level = "Easy"
            allow_hints = False
        elif difficulty == 2:
            max_num = 25
            max_attempts = 10
            level = "Medium"
            allow_hints = True
        else:
            max_num = 100
            max_attempts = 5
            level = "Hard"
            allow_hints = True

        rnd_number = random.randint(1, max_num)
        attempts = 0
        start_time = time.time()

        print(f"\nYou selected {level} mode. Guess a number between 1 and {max_num}.")
        if max_attempts != float('inf'):
            print(f"You have {max_attempts} attempts. Good luck! 🍀")

        while attempts < max_attempts:
            user_input = input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess (or type 'quit' to exit): ").strip().lower()

            if user_input == 'quit':
                print(f"Game over! Tata Bye-Bye Sayonara phir milenge dobara....😁 BTW the correct number was {rnd_number}🎯")
                return

            if not user_input.isdigit():
                print("Please enter a valid number.")
                continue

            guess = int(user_input)
            attempts += 1
            if guess < rnd_number:
                print("Too low! Try again.")
            elif guess > rnd_number:
                print("Too high! Try again.")
            else:
                end_time = time.time()
                total_time = round(end_time - start_time, 2)
                print(f"\nCongratulations🎉 You guessed the correct number {rnd_number} in {attempts} attempts and {total_time} seconds! 🕒")
                break

            #hints 
            if allow_hints and attempts < max_attempts:
                hint_request = input("Do you want a hint? (yes/no): ").strip().lower()
                if hint_request == 'yes':
                    hint = "Hint: "
                    if rnd_number % 2 == 0:
                        hint += "The number is even. "
                    else:
                        hint += "The number is odd. "
                    if rnd_number % 3 == 0:
                        hint += "It's also divisible by 3."
                    print(hint)

        else:
         
            print(f"\nOut of attempts! The correct number was {rnd_number}. Better luck next time! 😢")
        while True:
            retry = input("\nDo you want to play again? (yes/no): ").strip().lower()
            if retry in ['yes', 'no']:
                break
            else:
                print("Invalid input! Please enter 'yes' or 'no'.")

        if retry == 'no':
            print("Thanks for playing! Goodbye! 👋")
            break

# Run the game
guess_number()
