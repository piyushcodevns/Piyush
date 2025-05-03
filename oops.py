import matplotlib.pyplot as plt


class Regression:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        n = len(self.x)
        x2 = [i * i for i in self.x]
        y2 = [i * i for i in self.y]
        xy = [self.x[i] * self.y[i] for i in range(n)]

        sigma_x = sum(self.x)
        sigma_y = sum(self.y)
        sigma_x2 = sum(x2)
        sigma_y2 = sum(y2)
        sigma_xy = sum(xy)
        self.b = (n * sigma_xy - sigma_x * sigma_y) / (n * sigma_x2 - sigma_x**2)
        self.a = (sigma_y - self.b * sigma_x) / n
        self.r = (n * sigma_xy - sigma_x * sigma_y) / (
            (n * sigma_x2 - sigma_x**2) * (n * sigma_y2 - sigma_y**2)
        ) ** 0.5

    def __str__(self):
        return "self.x={0}, self.y={1}".format(self.a, self.b, self.r)

    # def makeGraph(self):
    #     plt.scatter(self.x, self.y, color="blue", label="Data Points")
    #     plt.plot(self.x, self.y, color="red", label="Regression Line")
    #     plt.xlabel("X-axis")
    #     plt.ylabel("Y-axis")
    #     plt.title("Regression Line and Data Points")
    #     plt.legend()
    #     plt.grid(True)
    #     plt.show()

    def getLine(self):
        n = len(self.x)
        x2 = [i * i for i in self.x]
        y2 = [i * i for i in self.y]
        xy = [self.x[i] * self.y[i] for i in range(n)]

        sigma_x = sum(self.x)
        sigma_y = sum(self.y)
        sigma_x2 = sum(x2)
        sigma_y2 = sum(y2)
        sigma_xy = sum(xy)

        self.b = (n * sigma_xy - sigma_x * sigma_y) / (n * sigma_x2 - sigma_x**2)
        self.a = (sigma_y - self.b * sigma_x) / n
        self.r = (n * sigma_xy - sigma_x * sigma_y) / (
            (n * sigma_x2 - sigma_x**2) * (n * sigma_y2 - sigma_y**2)
        ) ** 0.5

    def __str__(self):
        return "".format(self.a, self.b, self.r)


def straightLine(x, y, title):
    plt.fill_between(x, y, color="yellow", alpha=0.3)
    plt.plot(x, y, color="red", label="Regression Line")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()


def straightLine1(x2, y2, title):
    plt.fill_between(x2, y2, color="red", alpha=0.3)
    plt.plot(x2, y2, color="red", label="Regression Line")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()


x = [1, 2, 3, 4, 5, 6]
y = [33, 33, 32, 34, 37, 37]

straightLine(x, y, "Regression Line and Data Points")

x2 = [i * i for i in x]
y2 = [i * i for i in y]

straightLine1(x2, y2, "Regression Line and Data Points")


reg = Regression(x, y)

print(reg)

# reg.makeGraph()
