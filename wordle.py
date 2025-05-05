##Task 1
def task1_game():

    print("Welcome to Wordle. The player's goal is to guess a secret 5-letter word within 6 attempts.")

    secret_word = "phone"

    max_attempt = 6
    attempt = 0


    while attempt < max_attempt:
        player_guess = input("To begin, please enter 5 characters.").lower()

        if len(player_guess) != 5:
            print("You can only enter 5 letters, no more no less")
            continue
        attempt += 1
        remaining_attempt = max_attempt - attempt

        if player_guess == secret_word:
            print(f"Congrats, you guessed the word {secret_word}")
            break #not working, check later
        
        else:
            print(f"Wrong guess, remaining guesses: {remaining_attempt}")

    print(f"Game over, the word was: {secret_word}")
    break

task1_game()


