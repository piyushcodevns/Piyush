n = input("Enter the value of number")
n = int(n)
x, y = [], []
for i in range(n):
        newX = int(input("Enter the value of x"))
        x.append(newX)
        newY = int(input("Enter the value of y"))
        y.append(newY)

def getLine(x, y):
 n = len(x)
x2 = [i * i for i in x]
y2 = [i * i for i in y]
xy = [x[i] * y[i] for i in range(n)]
sigma_x = sum(x)             
sigma_y = sum(y)
sigma_x2 = sum(x2)
sigma_y2 = sum(y2)
sigma_xy = sum(xy)
b = (n * sigma_xy - sigma_x * sigma_y) / (n * sigma_x2 - sigma_x**2)
a = (sigma_y - b * sigma_x) / n
r = (n * sigma_xy - sigma_x * sigma_y) / (
    (n * sigma_x2 - sigma_x**2) * (n * sigma_y2 - sigma_y**2)
) ** 0.5

import matplotlib.pyplot as plt


def makeDataLineGraph(y, x, title):
    plt.plot(y, x, color="green", linewidth=2, label="Data Line")
    plt.fill_between(y, x, color="blue", alpha=0.3)
    plt.title(title)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.grid(True)
    plt.show()

    return a, b, r
a, b, r = makeDataLineGraph(y, x, title="Graph of y= x")  