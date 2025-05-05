##Task 1
def task1_game():

    print("Welcome to Wordle! You have 6 attempts to guess the correct 5-letter word!")

    secret_word = "phone"

    max_attempt = 6
    attempt = 0


    while attempt < max_attempt:
        player_guess = input("Please enter your guess: ").lower() #lower case upper case fixed here

        if len(player_guess) != 5:
            print("Please enter exactly 5 charactersi no more no less.")
            continue
        attempt += 1
        remaining_attempt = max_attempt - attempt

        if player_guess == secret_word:
            print(f"Congrats, you guessed the word {secret_word}")
            break 
            
        #task 2 from here, part inside else
        else:
            #hint 1:
            correct_letters = [letter for letter in player_guess if letter in secret_word]
            #if letters in player_guess match to letters in secret_word

            if correct_letters:
                print("These letters exist in the word:", ", ".join(set(correct_letters)) if correct_letters else "none") 
            
            #hint 2:
            correct_position = [str(i + 1) for i in range(5) if player_guess[i] == secret_word[i]] #else(none) part not working here, check back later
            if correct_position:
                print("These letter positions are already correct:", ", " .join(set(correct_position))) 

        
            print(f"Wrong guess, remaining guesses: {remaining_attempt}")

    print(f"Game finished, the word was: {secret_word}")

task1_game()


