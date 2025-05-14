weekday = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def get_month_name(month_number):
    if month_number < 1 or month_number > 12:
        return "Invalid month number"
    return month[month_number - 1]


def get_weekday_name(weekday_number):
    if weekday_number < 1 or weekday_number > 7:
        return "Invalid weekday number"
    return weekday[weekday_number - 1]


def display_month_and_weekday():
    month_number = int(input("Enter the month number (1-12): "))
    weekday_number = int(input("Enter the weekday number (1-7): "))
    month_name = get_month_name(month_number)
    weekday_name = get_weekday_name(weekday_number)
    print(f"Month: {month_name}")
    print(f"Weekday: {weekday_name}")


if __name__ == "__main__":
    display_month_and_weekday()


def printCalendar(noofdays, startweekday, month_name=""):
    for day in weekday:
        print(f"{day:5s}", end="")
    print()
    for i in range(1, startweekday + 1):
        print(f'{"":3s}', end="")
    for i in range(1, noofdays + 1):
        print(f"{str(i):4s}", end="")
        if (i + startweekday) % 7 == 0:
            print()
    print()


printCalendar(31, 3)
