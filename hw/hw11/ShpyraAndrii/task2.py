week_days = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)


def analyze_week_day(week_day):
    if week_day <= 0 or week_day > len(week_days):
        raise ValueError(f"Value should be between 1 and {len(week_days)}")
    result = week_days[week_day-1]
    print(f'The day is {result}')


def main():
    try:
        week_day = int(
            input(
                "Specify a day of the week (1 is Monday, 2 is Tuesday, etc.): "
                )
            )
        analyze_week_day(week_day)
    except ValueError as e:
        print(f"User specified invalid day of the week: {e}")


if __name__ == '__main__':
    main()
