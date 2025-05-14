import calendar

weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
months = [
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
week_names = ["I", "II", "III", "IV", "V", "VI"]

def show_calendar(month_number, starting_day):
    days = calendar.monthrange(2025, month_number)[1]
    print("\n", months[month_number - 1].center(35))

    for day in weekdays:
        print(f"{day:>4}", end="")
    print()
    day = 1
    count = 0
    for space in range(1, starting_day):
        print("    ", end="")

    for d in range(starting_day, 8):
        if day <= days:
            print(f"{day:>4}", end="")
            day += 1
    print()
    count += 1
    while day <= days:
        for d in range(7):
            if day <= days:
                print(f"{day:>4}", end="")
                day += 1
            else:
                print("    ", end="")
        else:
            print()


m = int(input("Enter month number (1-12): "))
s = int(input("Enter starting weekday (1=Mon to 7=Sun): "))
show_calendar(m, s)
