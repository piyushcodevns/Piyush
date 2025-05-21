from datetime import datetime


class Time:
    def __init__(self, hour, minute):
        if not (0 <= hour <= 23):
            raise ValueError("Hour must be between 0 and 23")
        if not (0 <= minute <= 59):
            raise ValueError("Minute must be between 0 and 59")
        self.hour = hour
        self.minute = minute

    def print_12hr_format(self):
        if self.hour == 0:
            hour_12 = 12
            period = "AM"
        elif 1 <= self.hour < 12:
            hour_12 = self.hour
            period = "AM"
        elif self.hour == 12:
            hour_12 = 12
            period = "PM"
        else:
            hour_12 = self.hour - 12
            period = "PM"
        print(f"{hour_12:02d}:{self.minute:02d} {period}")

t1 = Time(11, 45)
t1.print_12hr_format()
t2 = Time(12, 45)
t2.print_12hr_format()
t3 = Time(2, 5)
t3.print_12hr_format()
try:
    t4 = Time(0, 65)
    t4.print_12hr_format()
except ValueError as e:
    print("Error:", e)


today = datetime.now()
print(today.strftime("%d/%m/%Y"))
