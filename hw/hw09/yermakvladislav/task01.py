import random

def number_game(random_number):
    """
    Run a guessing game where the player tries to guess random_number in up to 10 attempts.
    """
    
    player_number = int(input("Guess the number from 1 to 100.\nYou have 10 attempts: "))
    attempt = 0
    while random_number != player_number:
        if attempt < 9:
            if player_number < random_number:
                player_number = int(input(f"{9 - attempt} attempts remaining. Try a larger number: "))
                attempt += 1
            else:
                player_number = int(input(f"{9 - attempt} attempts remaining. Try a smaller number."))
                attempt += 1
        else:
            return f"Game over! You lost! The number was {random_number}"
    else:
        return f"You won! The number was {random_number}"
        


print (number_game(random.randint(1, 100)))

