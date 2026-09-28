import random

if (__name__ == "__main__"):
    random_number = random.randint(1, 100)
    print("Я загадав рандомне число від 1 до 100, спробуйте вгадати його, у вас є 10 спроб")

    user_number = int(input())
    
    for i in range(1, 10):
        if (random_number > user_number):
            print("Рандомне число є більшим ніж ваше, спробуйте ще раз")
            user_number = int(input())
        elif (random_number < user_number):
            print("Рандомне число є меншим ніж ваше, спробуйте ще раз")
            user_number = int(input())
        else:
            print("Ви вгадали число, вітаю!!!")
            break
    else:
        print("Ви не відгадали число(((")