from random import randint

secret_number = randint(1, 100)
max_attempts = 10

print("Згенеровано число від 1 до 100. Є 10 спроб, щоб його відгадати.")

for attempt in range(1, max_attempts + 1):
    guess = int(input(f"Спроба {attempt}. Введіть число: "))
    
    if guess == secret_number:
        print(f"Ви успішно відгадали число {secret_number}!")
        break
    elif secret_number > guess:
        print("Загадане число більше ніж введене.")
    else:
        print("Загадане число менше ніж введене.")
        
else:
    print(f"Ви використали всі 10 спроб. Загадане число було: {secret_number}.")