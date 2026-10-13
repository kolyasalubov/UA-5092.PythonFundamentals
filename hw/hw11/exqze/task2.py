def day_of_week(number):
    days = {
        1: "monday",
        2: "tuesday",
        3: "wednesday",
        4: "thursday",
        5: "friday",
        6: "saturday",
        7: "sunday"
    }
    
    if number >= 8 or number < 1:
        return "invalid number, please enter a value from 1 to 7."
    
    return days[number]

try:
    user_num = int(input("enter a number from 1 to 7: "))
    result = day_of_week(user_num)
    print(result)
except ValueError:
    print("error: you have entered non numeric data.")