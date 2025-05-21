weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]  # Weekday names
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]  # Month names

def isLeapYear(year):
    """Check if a year is a leap year."""
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False

def getDaysInMonth(month, year):
    if month in [4, 6, 9, 11]:
        return 30
    if month == 2:  
        if isLeapYear(year):
            return 29
        else:
            return 28
    return 31  

def printCalendar(noofdays, startweekday, month_name):
    print(f"{month_name:^28}") 
    for day in weekdays:
        print(f"{day:5s}", end="")
    print()

    for i in range(1, startweekday + 1):
        print(f'{"":5s}', end="")
    for i in range(1, noofdays + 1):
        print(f"{str(i):5s}", end="")
        if (i + startweekday) % 7 == 0:
            print()
    print()

def main():
    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))

    if month < 1 or month > 12:
        print("Invalid month. Please enter a value between 1 and 12.")
        return

    month_name = months[month - 1]
    noofdays = getDaysInMonth(month, year)
    import calendar
    startweekday = calendar.monthrange(year, month)[0]  
    printCalendar(noofdays, startweekday, month_name)
if __name__ == "__main__":
    main()
