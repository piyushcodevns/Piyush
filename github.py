# Find the max of three numbers
# a = 5
# b = 4
# c = 6
# largest = 0
# if a >= b and a >= c:
#     largest = a
# elif b >= a and b >= c:
#     largest = b
# else:
#     largest = c
# print("The largest number is:", largest)


# Check for a leap year
# year=2030
# if (year %4==0 and year %100 !=0) or (year %400==0):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")
    
    
# Check the type of a Triangle. Is triangle possible, Equilateral, Isosceles, Scalene and Right Angled
# a=4
# b=5
# c=4
# if a==b and b==c:
#     print("Equilateral Triangle")
# elif a==b or b==c or c==a:
#     print("Isosceles Triangle")
# elif (a**2==b**2+c**2) or (b**2==a**2+c**2) or (c**2==a**2+b**2):
#     print("Right Angled Triangle")
# else:
#     print("Scalene Triangle")
    
# Check for pass, fail and division given marks in 3 subjects. 40 is passing marks. 3rd division >=40 <50, >=50 <60 2nd, >=60 1st.
# math=59
# science=60
# english=53

# avg =(math +science +english)/3

# if(math <40 or science <40 or english <40):
#     print("Fail")
# elif(avg < 50):
#     print("3rd Division")
# elif(avg  < 60):
#     print("2nd Division")
# elif(avg >= 60):
#     print("1st Division")
# else:
#     print("Invalid input")


# Find the days in month given the month no and year
month=2
year=2020
if month in [1,3,5,7,8,10,12]:
    print("31 days")
elif month in [4,6,9,11]:
    print("30 days")
elif month==2:
    if (year %4==0 and year %100 !=0) or (year %400==0):
        print("29 days")
    else:
        print("28 days")
else:
    print("Invalid month number")
    