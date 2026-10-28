from random import randint

def play_guessing_game(secret_number):
    """Запускає гру, де користувач має вгадати число за 10 спроб"""
    for attempt in range(1, 11):
        user_guess = int(input(f"Спроба {attempt}/10. Введіть ваше число: "))
        
        if user_guess == secret_number:
            print("Вітаємо! Ви вгадали число!")
            return
            
        elif user_guess < secret_number:
            print("Загадане число більше, ніж ваше.")
            
        else:
            print("Загадане число менше, ніж ваше.")
            
    print(f"На жаль, спроби вичерпано. Загадане число було: {secret_number}")

target_number = randint(1, 100)

play_guessing_game(target_number)
