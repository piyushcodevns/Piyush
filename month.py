weekdays=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
def month_days(month,year):
    if month in[1,3,5,7,8,10,12]:
        return 31
    elif month in[4,6,9,11]:
        return 30
    elif month==2:
        if year%4==0 and year%100!=0 or year%400==0:
            return 29
        else:
            return 28
    else:
        print("Invalid month")
        
def month_name(month):
    print("Enter the month")