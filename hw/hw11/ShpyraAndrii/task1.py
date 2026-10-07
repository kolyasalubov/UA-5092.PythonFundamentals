def analyze_age(user_age):
    if user_age < 0:
        raise ValueError('Age cannot be negative')
    result = 'even' if user_age % 2 == 0 else 'odd'
    print(f'The age is {result}')


def main():
    try:
        user_age = int(input('Please specify your age: '))
        analyze_age(user_age)
    except ValueError as e:
        print(f"User specified invalid value for the age: {e}")


if __name__ == '__main__':
    main()
