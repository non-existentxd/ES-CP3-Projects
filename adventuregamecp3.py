import random


# Function for ending
def earth():
    print("You find yourself in a small, simple room with a single door. On a pedestal in the center of the room lies a shimmering key, glowing with an otherworldly light. The air feels lighter here, and there's a sense of calm and completion. This is the final step before returning to reality.")
# Initialize player stats and game variables
player_stats = {
    'health': 100,
    'agility': 10,
    'strength': 10
}

items = ['Health Potion', 'Strength Boost', 'Agility Boost']

# Define enemies
enemies = {
    'Boogie1': {'health': 3},
    'Boogie2': {'health': 5},
    'FinalBoss': {'health': 10}
}

# Function to display the player's stats
def display_stats():
    print(f"Health: {player_stats['health']}, Agility: {player_stats['agility']}, Strength: {player_stats['strength']}")

#Function for Ending credits
def ending_credits():
    print("Ending credits: ")
    print("-non.existent :P")
    print("Aka: Emeraude (o^-')b")
    print("see ya soon!!!")


# Function for Tic Tac Toe mini-game
def play_tic_tac_toe():
    board = [' ' for _ in range(9)]
    
    def print_board():
        for i in range(1):
            print("EXAMPLE:")
            print("1|2|3")
            print("-+-+-")
            print("4|5|6")
            print("-+-+-")
            print("7|8|9")
            print(" ")
            print(" ")
        print(f"{board[0]}|{board[1]}|{board[2]}")
        print("-+-+-")
        print(f"{board[3]}|{board[4]}|{board[5]}")
        print("-+-+-")
        print(f"{board[6]}|{board[7]}|{board[8]}")
    
    def check_win():
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for condition in win_conditions:
            if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
                return board[condition[0]]
        return None
    
    def player_move():
        while True:
            try:
                move = int(input("Choose a position (1-9): ")) - 1
                if board[move] == ' ':
                    board[move] = 'X'
                    break
                else:
                    print("Position already taken.")
            except (IndexError, ValueError):
                print("Invalid input. Choose a number between 1 and 9.")

    def computer_move():
        empty_positions = [i for i, x in enumerate(board) if x == ' ']
        move = random.choice(empty_positions)
        board[move] = 'O'

    print_board()
    for _ in range(5):
        player_move()
        if check_win() == 'X':
            print_board()
            return "win"
        if ' ' not in board:
            print_board()
            return "tie"
        computer_move()
        if check_win() == 'O':
            print_board()
            return "lose"
        print_board()
    return "tie"

# Function for Hangman mini-game
def play_hangman():
    words = ['dream', 'adventure', 'challenge']
    word = random.choice(words)
    guessed_letters = set()
    attempts = 6

    def display_word():
        return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

    print("Welcome to Hangman!")
    while attempts > 0:
        print(display_word())
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        guessed_letters.add(guess)
        if guess in word:
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                return "win"
        else:
            attempts -= 1
            print(f"Wrong guess. Attempts left: {attempts}")
    print(f"Out of attempts. The word was: {word}")
    return "lose"

# Function for Pig mini-game
def play_pig_game():
    def player_roll():
        return random.randint(1, 6)
    
    def player_turn():
        total = 0
        while True:
            roll = player_roll()
            print(f"Player rolled: {roll}")
            if roll == 1:
                return 0
            total += roll
            choice = input("Roll again or hold? (r/h): ").lower()
            if choice == 'h':
                return total
    
    def computer_turn():
        total = 0
        while total < 20:
            roll = player_roll()
            print(f"Final boss rolled: {roll}")
            if roll == 1:
                return 0
            total += roll
        return total

    player_score = player_turn()
    print(f"Player score: {player_score}")
    if player_score == 0:
        return "lose"
    
    computer_score = computer_turn()
    print(f"Final boss: {computer_score}")
    if computer_score >= player_score:
        return "lose"
        
    return "win"

# Function to handle combat
def combat1(opponent_name):
    opponent = enemies[opponent_name]
    print(f"A {opponent_name} with {opponent['health']} health challenges you!")

    while player_stats['health'] > 0 and opponent['health'] > 0:
        print(f"{opponent_name}'s health: {opponent['health']}")
        print("Choose your action:")
        print("1) Attack")
        print("2) Use Item")
        print("3) Defend")
        print("4) Flee")
        choice = input("Action: ")
        
        if choice == '1':
            print("You attack!")
            opponent['health'] -= 1
            print(f"{opponent_name}'s health: {opponent['health']}")
            
        elif choice == '2':
            if items:
                item = items.pop()
                print(f"You use {item}.")
                if item == 'Health Potion':
                    player_stats['health'] += 20
                    print("Health increased by 20.")
                elif item == 'Strength Boost':
                    player_stats['strength'] += 5
                    print("Strength increased by 5.")
                elif item == 'Agility Boost':
                    player_stats['agility'] += 5
                    print("Agility increased by 5.")
            else:
                print("No items available.")
                
        elif choice == '3':
            print("You defend. You will take less damage from the next attack.")
            defense_active = True
            
        elif choice == '4':
            print("You flee.")
            return False  # Fleeing is not allowed in combat

        # Opponent's turn to attack
        if opponent['health'] >= 0:
            if 'defense_active' in locals():
                player_damage = 0  # No damage due to defense
                del defense_active
            else:
                player_damage = 5  # Standard damage
            player_stats['health'] -= player_damage
            print(f"You take {player_damage} damage. Current health: {player_stats['health']}")
            if player_stats['health'] <= 0:
                print("You have been defeated!")
                return False
        
        if opponent['health'] <= 0:
            print(f"You defeated the {opponent_name}.")
            return True
        

# Function to handle combat
def combat2(opponent_name):
    opponent = enemies[opponent_name]
    print(f"A {opponent_name} with {opponent['health']} health challenges you!")

    while player_stats['health'] > 0 and opponent['health'] > 0:
        print(f"{opponent_name}'s health: {opponent['health']}")
        print("Choose your action:")
        print("1) Attack")
        print("2) Use Item")
        print("3) Defend")
        choice = input("Action: ")
        
        if choice == '1':
            print("You attack!")
            opponent['health'] -= 1
            print(f"{opponent_name}'s health: {opponent['health']}")
            
        elif choice == '2':
            if items:
                item = items.pop()
                print(f"You use {item}.")
                if item == 'Health Potion':
                    player_stats['health'] += 20
                    print("Health increased by 20.")
                elif item == 'Strength Boost':
                    player_stats['strength'] += 5
                    print("Strength increased by 5.")
                elif item == 'Agility Boost':
                    player_stats['agility'] += 5
                    print("Agility increased by 5.")
            else:
                print("No items available.")
                
        elif choice == '3':
            print("You defend. You will take less damage from the next attack.")
            defense_active = True


        # Opponent's turn to attack
        if opponent['health'] > 0:
            if 'defense_active' in locals():
                player_damage = 0  # No damage due to defense
                del defense_active
            else:
                player_damage = 5  # Standard damage
            player_stats['health'] -= player_damage
            print(f"You take {player_damage} damage. Current health: {player_stats['health']}")
            if player_stats['health'] <= 0:
                print("You have been defeated!")
                return False
        
        if opponent['health'] <= 0:
            print(f"You defeated the {opponent_name}.")
            return True
        


# Main game function
def main_game():
    current_location = "Room1"
    
    while current_location != "Room9":
        if current_location == "Room1":
            print("You wake up in a dream. This place is like a galaxy that seems to stretch endlessly in all directions. The sky is a swirling mass of colors, and the ground beneath you shifts as if it’s made of liquid. There are faint echoes that fill the air. A shimmering portal stands before you, its light beckoning you forward. This is where your dream begins.")
            print(" ")
            action = input("Do you enter the portal? (yes/no): ").lower()
            if action == 'yes':
                current_location = "Room2"
            else:
                print("You remain in The Other World.")

        elif current_location == "Room2":
            print("You step through the portal and find yourself in blinding lights. The walls and floor are pure white, and everything appears to glow. There’s an ethereal quality to the light, and it feels like you could almost touch it. The light seems to lead towards an exit on the far side of the room.")
            print(" ")
            action = input("Do you move forward to the Cold Room? (yes/no): ").lower()
            if action == 'yes':
                current_location = "Room3"
            else:
                print("You return to The Other World.")

        elif current_location == "Room3":
            print("You enter a room where the walls are covered in frost, and your breath forms clouds in the freezing air. Snowflakes gently fall from above, and a chilling wind seems to whisper through the space. A frosty mist obscures the path forward, leading you deeper into the cold.")
            print(" ")
            action = input("Do you move forward to the Hot Room? (yes/no): ").lower()
            if action == 'yes':
                current_location = "Room4"
            else:
                print("You return to The Bright Room.")

        elif current_location == "Room4":
            print("The heat hits you like a wave as you step into this room. The walls are lined with glowing red and orange stones, and the air is thick with sweltering warmth. Puffs of steam rise from cracks in the floor, and the heat makes it difficult to breathe. There’s a sense of intense energy in the room.")
            print(" ")
            action = input("Do you move forward to the Sword Room? (yes/no): ").lower()
            if action == 'yes':
                current_location = "Room5"
            else:
                print("You return to The Cold Room.")

        elif current_location == "Room5":
            print("You are in The Sword Room. A Boogie with 3 health challenges you.")
            if combat1('Boogie1'):
                current_location = "Room6"
            else:
                print("You are forced to return to The Hot Room.")
                current_location = "Room4"

        elif current_location == "Room6":
            print("You are in The Shield Room. A Boogie with 5 health challenges you.  NOTE: YOU CANNOT FLEE >:) .")
            if combat2('Boogie2'):
                current_location = "Room7"
            else:
                print("You are forced to return to The Sword Room.")
                current_location = "Room5"

        elif current_location == "Room7":
            print("You enter a lush, verdant garden where every plant and flower seems to radiate vitality. The air is fresh and fragrant, and a gentle breeze rustles the leaves. In the center of the garden are sprouts who invite you to play a game. The garden feels rejuvenating, and you notice that your energy is slowly being restored.")
            print(" ")
            player_stats['health'] = 100
            print("You play a game of Tic Tac Toe with the sprouts.")
            if play_tic_tac_toe() == "win":
                print("You won Tic Tac Toe!")
                print("You gain 15 health")
                player_stats['health'] = 115
            else:
                print("You lost Tic Tac Toe.")
                print("You lose 15 health")
                player_stats['health'] = 85
            current_location = "Room8"

        elif current_location == "Room8":
            print("You are in The Final Room. The Final Boss with 10 health challenges you. NOTE: YOU CANNOT FLEE! >:) .")
            if combat2('FinalBoss'):
                if enemies['FinalBoss']['health'] == 1:
                    print("The Final Boss is on its last health. It chooses a game to play.")
                    game_choice = random.choice(['Tic Tac Toe', 'Hangman', 'Pig'])
                    if game_choice == 'Tic Tac Toe':
                        if play_tic_tac_toe() == "win":
                            print("You defeated the Final Boss in Tic Tac Toe!")
                            current_location = "Room9"
                        else:
                            print("You lost the game. You return to The Garden Room.")
                            current_location = "Room7"
                    elif game_choice == 'Hangman':
                        if play_hangman() == "win":
                            print("You defeated the Final Boss in Hangman!")
                            current_location = "Room9"
                        else:
                            print("You lost the game. You return to The Garden Room.")
                            current_location = "Room7"
                    elif game_choice == 'Pig':
                        if play_pig_game() == "win":
                            print("You defeated the Final Boss in Pig!")
                            current_location = "Room9"
                        else:
                            print("You lost the game. You return to The Garden Room.")
                            current_location = "Room7"
                else:
                    print("You defeated the Final Boss!")
                    current_location = "Room9"
            else:
                print("You are forced to return to The Shield Room.")
                current_location = "Room6"


    print("Congratulations! but this time the Final Boss wants to play a mini game against you. . .")
    print("Pick a game (you will never know which of these they are) 1) 2) 3):")
    choice =input("Pick a game: ")
    if choice == '1':
        print("This is game of pig")
        if play_pig_game() == "win":
            print("You win the Game of Pig!")
            print(" ")
            earth()
            print(" ")
            ending_credits()
            print(" ")
        else:
            print("You lost in Game of Pig")
            print("Better luck next time!")
            print(" ")
            print("You are stuck in this dream world forever. ")
            print(" ")
            ending_credits()
            print(" ")
    elif choice == '2':
        print("This is tic tac toe")
        if play_tic_tac_toe() == "win":
            print("You won Tic Tac Toe!")
            print(" ")
            earth()
            print(" ")
            print(" ")
        else:
            print("You lost Tic Tac Toe.")
            print("Better luck next time!")
            print(" ")
            print("You are stuck in this dream world forever. ")
            print(" ")
            print(" ")
    elif choice == '3':
        if play_hangman() == "win":
            print("You won in the game of hangman")
            print(" ")
            earth()
            print(" ")
            print(" ")
        else:
            print("You lost in hangman")
            print(" ")
            print("You are stuck in this dream world forever. ")
            print(" ")
            print(" ")
    else:
        print("invalid input")
        

    


# Start the game
main_game()
print(" ")
print(" ")
print(" ")
print("The End ")
print(" ")
print(" ")
print(" ")
ending_credits()