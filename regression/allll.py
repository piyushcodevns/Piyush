import matplotlib.pyplot as plt

class RegressionPredictor:
    def __init__(self, x, y, company_name=""):
        self.x = x
        self.y = y
        self.n = len(x)
        self.company_name = company_name

        self.sigmax = sum(x)
        self.sigmay = sum(y)
        self.x2 = [i * i for i in x]
        self.sigmax2 = sum(self.x2)
        self.sigmay2 = sum([i * i for i in y])
        self.sigmaxy = sum([x[i] * y[i] for i in range(self.n)])

        # Slope (b) and intercept (a)
        self.b = ((self.n * self.sigmaxy) - (self.sigmax * self.sigmay)) / \
                 ((self.n * self.sigmax2) - (self.sigmax ** 2))
        self.a = (self.sigmay - self.b * self.sigmax) / self.n

        # Correlation coefficient (r)
        numerator = self.sigmaxy - (self.sigmax * self.sigmay / self.n)
        denominator = ((self.sigmax2 - (self.sigmax ** 2 / self.n)) *
                       (self.sigmay2 - (self.sigmay ** 2 / self.n))) ** 0.5
        self.r = numerator / denominator if denominator != 0 else 0

    def predict(self, x_values):
        return [self.a + self.b * x for x in x_values]

    def __str__(self):
        return (f"x: {self.x}\n"
                f"y: {self.y}\n"
                f"x2: {[i * i for i in self.x]}\n"
                f"y2: {[i * i for i in self.y]}\n"
                f"a: {self.a:.3f}\n"
                f"b: {self.b:.3f}\n"
                f"r: {self.r:.3f}\n")
                

    def plot(self, diagram_title, plot_title, xlabel, ylabel):
        plt.figure(figsize=(8, 6))
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(f"{plot_title} - {self.company_name}")
        plt.grid(True)

        # Original data and regression line
        regression_data = self.predict(self.x)
        plt.plot(self.x, self.y, 'ro-', label=diagram_title)
        plt.plot(self.x, regression_data, 'g--', label="Line of Best Fit")

        # Prediction for extra inputs
        predict_input = [i for i in range(1, 9)]
        predict_output = self.predict(predict_input)
        plt.plot(predict_input, predict_output, 'y-.', label="Predicted Value")

        plt.legend()
        plt.show()