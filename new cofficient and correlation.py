import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7]
y = [2, 3, 4, 5, 6, 7, 9]

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

    return a, b, r

result= getLine(x, y)

def makeDataLineGraph(x, y, title):
    a, b, r = getLine(x, y) 
    plt.plot(x, y, color="green", linewidth=2, label="Data Line")
    plt.fill_between(x, y, color="blue", alpha=0.3)
    plt.title(title) 
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.grid(True)
    plt.show()

makeDataLineGraph(x, y, title="Graph of y= x")

x2 = [i * i for i in x]
y2 = [i * i for i in y]
makeDataLineGraph(x2, y2, title="Graph of y= x^2")



def makeFilledGraph(x, y, title):
    plt.plot(x, y, color="orange", linewidth=2, label="Data Line")
    plt.fill_between(x, y, color="yellow", alpha=0.3)
    plt.title(title)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True, alpha=0.5)
    plt.legend()
    plt.show()

makeFilledGraph([1, 2, 3, 4, 5, 6, 7, 8], [33, 33, 32, 34, 37, 37, 37, 37], "Filled Graph Example")