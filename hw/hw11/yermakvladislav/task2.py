def day_of_the_week():
    
    day = input("Enter the day of the week: ")
    
    try:
        day = int(day)
    except (ValueError, TypeError):
        return "You entered not a number."
    
    
    if 0 < day < 8:
        if day == 1:
            return "Monday"
        elif day == 2:
               return "Tuesday"
        elif day == 3:
            return "Wednesday"
        elif day == 4:
            return "Thursday"
        elif day == 5:
            return "Friday"
        elif day == 6:
            return "Saturday"
        else:
            return "Sunday"
    else:
        return "You entered an incorrect day of the week."



print(day_of_the_week())
