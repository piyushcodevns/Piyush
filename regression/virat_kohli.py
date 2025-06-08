import matplotlib.pyplot as plt

class RegressionPredictor:
    def __init__(self, x, y, projecttitle, xname="X", yname="Y"):
        self.x = x
        self.y = y
        self.projecttitle = projecttitle
        self.xname = xname
        self.yname = yname
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
        return(
            f"--- Regression Summary for {self.projecttitle} ---\n"
            f"{self.xname} values: {self.x}\n"
            f"{self.yname} values: {self.y}\n"
            f"{self.xname}^2: {[i * i for i in self.x]}\n"
            f"{self.yname}^2: {[i * i for i in self.y]}\n"
            f"Intercept (a): {self.a:.3f}\n"
            f"Slope (b): {self.b:.3f}\n"
            f"Correlation coefficient (r): {self.r:.3f}\n")
        

    def plot(self, diagram_title, plot_title, xlabel=None, ylabel=None):
        plt.figure(figsize=(9, 6))
        plt.title(plot_title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True, linestyle='--', alpha=0.6)
        regression_data = self.predict(self.x)
        plt.plot(self.x, self.y, "o-", label=diagram_title, color="#1f77b4", markersize=8)
        plt.scatter(self.x, self.y, color="#1f77b4")
        plt.plot(self.x, regression_data, "g--", label="Line of Best Fit", linewidth=2)
        plt.legend()
        plt.show()