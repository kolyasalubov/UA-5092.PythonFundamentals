def analyze_day_of_week():
    """
    Запитує в користувача число й повертає відповідний день тижня.
    Обробляє нечислові вхідні дані та числа за межами діапазону 1-7.
    """
    
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    
    user_input = input("Enter a number (1-7) for the day of the week: ")
    
    try:
        number = int(user_input)
        
        if number in days:
            print(f"Day {number} corresponds to {days[number]}.")
        else:
            print(f"Invalid input: {number}. Please enter a number between 1 and 7.")
            
    except ValueError:
        print("Error: Invalid input. You must enter a numerical value.")

if __name__ == "__main__":
    analyze_day_of_week()


