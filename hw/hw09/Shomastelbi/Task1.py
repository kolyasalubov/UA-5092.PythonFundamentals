from random import randint

def guess_rand_num():
    """
    This function compares number from input
    with random number in range from 1 to 100.
    User has to guess the number in within 10 attempts
    """
    print("You have 10 attempts to guess the number in range from 1 to 100")

    rand_num = randint(1, 100)
    total_attempts = 10
    cur_attempt = 1

    while cur_attempt <= total_attempts:
        guess_num = int(input(f"Attempt №{cur_attempt}. Enter your number: "))

        if guess_num == rand_num:
            return f"Correct! Number of attempts - {cur_attempt}"
        elif guess_num < rand_num:
            print(f"{guess_num} is smaller then wished number")
        elif guess_num > rand_num:
            print(f"{guess_num} is bigger then wished number")

        cur_attempt +=1
    return "Sorry, you lost("

if __name__ == '__main__':
    guess_rand_num()
