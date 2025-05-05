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
                print("These letters exist in the word:")
                for letter in correct_letters:
                    print(letter, end=' ')
                print()  #simplified version to see why "none" isnt working
            
            #hint 2:
            correct_position = []
            for i in range(5):
                if player_guess[i] == secret_word[i]:
                    correct_position.append(str(i + 1))
            #if guessed letter exists in secret word print position of string

            if correct_position:
                print("These letter positions are already correct:")
                for pos in correct_position:
                    print(pos, end=' ')
                print() #simplified version to see why "none" isnt working, and still not working check later
        
            print(f"Wrong guess, remaining guesses: {remaining_attempt}")

    print(f"Game finished, the word was: {secret_word}")

task1_game()


