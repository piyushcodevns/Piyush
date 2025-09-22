import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [5, 6, 7, 8, 9, 10]


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
    r = (n * sigma_xy - sigma_x * sigma_y) / ((n * sigma_x2 - sigma_x**2) * (n * sigma_y2 - sigma_y**2)) ** 0.5
    return a, b, r


def makeDataLineGraph(y2, x2, title):
    plt.plot(y2, x2, color="green", linewidth=2, label="Data Line")
    plt.fill_between(y2, x2, color="blue", alpha=0.3)
    plt.title(f" a={a:.3f} , b={b:.3f}, r={r:.3f}")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.grid(True)
    plt.show()


print("Hello Python")
a, b, r = getLine(x, y)

makeDataLineGraph(y, x, title="Graph of y= x")
