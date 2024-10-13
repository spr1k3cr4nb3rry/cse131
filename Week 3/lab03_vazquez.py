# Name: Izzie Vazquez
# Assignment Name: Lab 03: Calendar Program
# Assignment Description: 
#   - Create a calendar for any month of any year from 1753 forward. This program is similar to the cal utility on the Linux system. It will manually compute how to display the calendar for a given month without using Python's datetime (or any other) library. It will start by prompting the user for the numeric month and year to be displayed. When the program prompts the user for a month, only the values 1 through 12 are accepted. Any other input will yield a re-prompt. The same is true with years; the user input must be greater than 1752. Your program must know the number of days in a given month. This includes February, which is 28 or 29 days depending on whether it is a leap year. In other words, it must take leap years into account.  Your program must know the day of the week for the 1st of a given month. This must work for any month in any year from 1753 onward. We start with that year because the Gregorian calendar (the calendar we all use today) began on the 14th of September, 1752. To accomplish this feat, your program must tabulate the number of days between January 1, 1753 and the 1st of the month that you will be displaying. Note that January 1, 1753 was a Monday. 
# Reflection:
#   - The most difficult part of this program for me was actually the printing of the display_calendar() function. I ended up with a loop to print every day in a range, and made sure to add proper spacing so the calendar would appear nice and neat as opposed to a huge mess.
# Time taken: 
#   - Approximately 2 hours.

def get_month():
    '''Prompts user for month, then validates the user input for month.'''
    while True:
        try:
            month = int(input("Enter month (mm): "))
            if 1 <= month <= 12:
                return month
            else:
                print("Invalid month. Please enter a value between 01 and 12.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_year():
    '''Prompts user for year, then validates the user input for year.'''
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

def days_in_month(month, year):
    '''Gets the number of days in a given month for a specified year.'''
    if month == 2: return 29 if is_leap_year(year) else 28
    elif month in [4, 6, 9, 11]: return 30
    else: return 31

def days_since_1753(year, month):
    '''Calculates the total number of days between 01/01/1753 and the first day of the given month/year.'''
    total_days = 0
    for y in range(1753, year): total_days += 366 if is_leap_year(y) else 365
    for m in range(1, month): total_days += days_in_month(m, year)
    return total_days

def month_start(year, month):
    '''Gets the day of the week for the 1st of the month.'''
    days = days_since_1753(year, month)
    return (days + 1) % 7

def display_calendar(month, year):
    '''Displays the calendar for a given month/year.'''
    days = days_in_month(month, year)
    start_day = month_start(year, month)

    print("Su Mo Tu We Th Fr Sa")

    for _ in range(start_day): print("   ", end="")

    for day in range(1, days + 1):
        print(f"{day:2d} ", end = "")
        if (start_day + day) % 7 == 0: print()

    print("\n")

def main():
    '''Driver code of the algorithm.'''
    month, year = get_month(), get_year()
    display_calendar(month, year)
    
if __name__ == "__main__":
    main()