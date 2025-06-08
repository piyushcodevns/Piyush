import matplotlib.pyplot as plt

class RegressionPredictor:
    def __init__(self, x, y, wickets):
        self.x = x
        self.y = y
        # self.projecttitle = projecttitle
        self.wickets = wickets
        self.n = len(x)

        self.sigmax = sum(x)
        self.sigmay = sum(y)
        self.x2 = [i * i for i in x]
        self.sigmax2 = sum(self.x2)
        self.sigmay2 = sum([i * i for i in y])
        self.sigmaxy = sum([x[i] * y[i] for i in range(self.n)])
        self.b = ((self.n * self.sigmaxy) - (self.sigmax * self.sigmay)) / (
            (self.n * self.sigmax2) - (self.sigmax**2)
        )
        self.a = (self.sigmay - self.b * self.sigmax) / self.n
        numerator = self.sigmaxy - (self.sigmax * self.sigmay / self.n)
        denominator = (
            (self.sigmax2 - (self.sigmax**2 / self.n))
            * (self.sigmay2 - (self.sigmay**2 / self.n))
        ) ** 0.5
        self.r = numerator / denominator

    def predict(self, x_values):
        return [self.a + self.b * x for x in x_values]

    def __str__(self):
        return ( 
            f"x: {self.x}\n"
            f"y: {self.y}\n"
            f"x2: {[i * i for i in self.x]}\n"
            f"y2: {[i * i for i in self.y]}\n"
            f"a: {self.a:.3f}\n"
            f"b: {self.b:.3f}\n"
            f"r: {self.r:.3f}\n"
        )

    def plot(self, diagram_title, plot_title, xlabel, ylabel):
        plt.figure(figsize=(8, 6))
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(plot_title)
        plt.grid(True)
        regression_data = self.predict(self.x)
        plt.plot(self.x, self.y, "o-", label=diagram_title)
        plt.plot(self.x, regression_data, "g-", label="Line of Best Fit")
        plt.scatter(self.x, self.y, color="blue")
        plt.legend()
        plt.show()

    def plotX(self, diagram_title, plot_title, xlabel, ylabel):
        plt.figure(figsize=(8, 6))
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(plot_title)
        plt.grid(True)
        regression_data = self.predict(self.x)
        plt.plot(self.x, self.wickets, "o-", label=diagram_title)
        plt.plot(self.x, regression_data, "g-", label="Line of Best Fit")
        plt.scatter(self.x, self.wickets, color="blue")
        plt.legend()
        plt.show()