from random import randint

# Pick a random number from 1 to 100
random_number = randint(1, 100)
print(random_number)
attempt_counter = 0

while attempt_counter < 10:
    user_number = int(input("Guess a random number from 1 to 100: "))
    attempt_counter += 1
    if user_number > random_number:
        print(
            f"You number {user_number} is greater that a random number. "
            f"{10 - attempt_counter} attempts are left."
        )
    elif user_number < random_number:
        print(
            f"You number {user_number} is less that a random number. "
            f"{10 - attempt_counter} attempts are left."
        )
    else:
        print(f"Congratulations! You did it! {random_number} is a random number!")
        break

if attempt_counter >= 10 and user_number != random_number:
    print("Game over!")