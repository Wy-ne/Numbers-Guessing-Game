import random

# Store the number of guesses allowed for each difficulty
level_difficulty = {
    "easy": 10,
    "medium": 7,
    "hard": 5 
}

# Define a function called 'choose_difficulty' and return the number of tries
def choose_difficulty():
    while True:
        print("\nChoose a difficulty:")
        print("1. Easy - 10 tries")
        print("2. Medium - 7 tries")
        print("3. Hard - 5 tries")

        choice = input("Enter 1, 2, or 3: ").strip()
        if choice == "1":
            return level_difficulty["easy"]
        elif choice == "2":
            return level_difficulty["medium"]
        elif choice == "3":
            return level_difficulty["hard"]
        else:
            print("Invalid choice. Please try again.")

# Create a second function known as 'give_hint' to give a player a hint after 3 wrong guesses
def give_hint(secret_number, attempts_used):
    print("\nHint:")

    if attempts_used == 3:
        if secret_number % 2 == 0:
            print("The number is even.")
        else:
            print("The number is odd.")
    elif attempts_used == 4:
        if secret_number % 3 == 0:
            print("The number is divisible by 3.")
        else:
            print("The number is NOT divisible by 3.")
    else:
        if secret_number <= 50:
            print("The number is between 1 and 50.")
        else:
            print("The number is between 51 and 100.")

# Create the third function called 'play_game' to start playing
def play_game():
     print("\nWelcome to the Number Guessing Game!")
     print("I am thinking of a number between 1 and 100.")

     max_attempts = choose_difficulty()
     secret_number = random.randint(1,100)

     attempts_used = 0
     guessed_correctly = False

     while attempts_used < max_attempts:
         remaining_attempts = max_attempts - attempts_used
         print(f"\nYou have {remaining_attempts} guesses remaining.")
         try:
            guess = int(input("Enter your guess: "))
         except ValueError:
             print("Please enter a whole number.")
             continue

         if guess < 1 or guess > 100:
             print("Your guess must be between 1 and 100")
             continue
         attempts_used += 1 # Increasing the attempts used by 1

         if guess == secret_number:
             print(f"\nCongratulations! You guessed the number in {attempts_used} attempts.")
             guessed_correctly = True
             break
         elif guess > secret_number:
             print("Too High!")
         else:
             print("Too Low!")

        # Give a hint after 3 wrong guesses
         if attempts_used >= 3:
             give_hint(secret_number, attempts_used)
     if not guessed_correctly:
         print(f"\nGame over! You ran out of guesses.")
         print(f"The correct number was {secret_number}.")

     return guessed_correctly, attempts_used, max_attempts

# Create the fourth function called 'calculate_score' 
def calculate_score(guessed_correctly, attempts_used, max_attempts):
    if guessed_correctly:
        return max_attempts - attempts_used
    return 0

# Create the fifth function 'save_score'
def save_score(name, score):
    # Save the player's name and score to a text file.
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name},{score}\n")

# Create the final function known as 'show_leaderboard' to read the scores and display the top 5 players
def show_leaderboard():
    try:
        with open("leaderboard.txt", "r") as file:
            lines = file.readlines()

    except FileNotFoundError:
        print("\nNo scores have been saved yet.")
        return

    scores = []
    for line in lines:
        line = line.strip()

        if line:
            name, score = line.split(",")
            scores.append((name, int(score)))

    # Sort score from highest to lowest
    scores.sort(key=lambda player: player[1], reverse=True)

    print("\n----- LEADERBOARD -----")
    if not scores:
        print("No scores have been saved yet.")
    else:
        position = 1
        for name, score in scores[:5]:
            print(f"{position}. {name} - {score} points")
            position += 1
    print("----------------")

# Create a function known as 'main' to control the main game loop
def main():
    while True:
        guessed_correctly, attempts_used, max_attempts = play_game()
        score = calculate_score(guessed_correctly, attempts_used, max_attempts)

        print(f"\nYour score is: {score}")

        name = input("Enter your name for the leaderboard: ")
        save_score(name, score)

        show_leaderboard()

        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()

        if play_again != "yes":
            print("Thanks for playing!")
            break

# Start the game
main()




