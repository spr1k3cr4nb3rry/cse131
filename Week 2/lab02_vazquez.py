def get_valid_month():
    '''Validates the user input for month.'''
    while True:
        try:
            month = int(input("Enter month (mm): "))
            if 1 <= month <= 12:
                return month
            else:
                print("Invalid month. Please enter a value between 01 and 12.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_valid_year():
    '''Validates the user input for year.'''
    while True:
        try:
            year = int(input("Enter year (yyyy): "))
            if year > 1752:
                return year
            else:
                print("Invalid year. The year must be greater than 1752.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def is_leap_year(year):
    '''Checks if year is a leap year.'''
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0: return True
            else: return False
        else: return True
    else: return False

def get_days_in_month(month, year):
    '''Gets the number of days in a given month for a specified year.'''
    if month == 2: return 29 if is_leap_year(year) else 28
    elif month in [4, 6, 9, 11]: return 30
    else: return 31

def calculate_days_since_1753(year, month):
    '''Calculates the total number of days between 01/01/1753 and the first day of the given month/year.'''
    total_days = 0
    for y in range(1753, year): total_days += 366 if is_leap_year(y) else 365
    for m in range(1, month): total_days += get_days_in_month(m, year)
    return total_days

def get_start_day_of_month(year, month):
    '''Gets the day of the week for the 1st of the month.'''
    days_since_1753 = calculate_days_since_1753(year, month)
    return (days_since_1753 + 1) % 7

def display_calendar(month, year):
    '''Displays the calendar for a given month/year.'''
    days_in_month = get_days_in_month(month, year)
    start_day = get_start_day_of_month(year, month)

    print(f"\n   {month}/{year}")
    print("Mo Tu We Th Fr Sa Su")

    for _ in range(start_day): print("   ", end="")

    for day in range(1, days_in_month + 1):
        print(f"{day:2d} ", end = "")
        if (start_day + day) % 7 == 0: print()

    print("\n")

def main():
    '''Driver code of the algorithm.'''
    month, year = get_valid_month(), get_valid_year()
    display_calendar(month, year)
    
if __name__ == "__main__":
    main()