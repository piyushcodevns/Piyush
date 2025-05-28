import matplotlib.pyplot as plt


class regression:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        n = len(self.x)
        self.x2 = [i * i for i in self.x]
        self.y2 = [i * i for i in self.y] 
        xy = [self.x[i] * self.y[i] for i in range(n)]
        sigma_x = sum(self.x)
        sigma_y = sum(self.y)
        sigma_x2 = sum(self.x2)
        sigma_y2 = sum(self.y2)
        sigma_xy = sum(xy)
        self.b = (n * sigma_xy - sigma_x * sigma_y) / (n * sigma_x2 - sigma_x**2)
        self.a = (sigma_y - self.b * sigma_x) / n
        self.r = (n * sigma_xy - sigma_x * sigma_y) / (
            ((n * sigma_x2 - sigma_x**2) * (n * sigma_y2 - sigma_y**2)) ** 0.5
        )
 
    def __str__(self):
        return f"a = {self.a}\n,b = {self.b}\n, r = {self.r}"
    

    def plotXY(self, digramtitle, plottitle, xtitle, ytitle):

        plt.plot(self.x, self.y, label=digramtitle)
        plt.scatter(self.x, self.y, color='blue', label='Data Points')
        plt.title(plottitle)
        plt.xlabel(xtitle)
        plt.ylabel(ytitle)
        plt.legend()
        plt.grid(True)
        plt.show()


    def plotXX2(self, digramtitle, plottitle, xtitle, ytitle):

        plt.plot(self.x, self.y, label=digramtitle)
        plt.scatter(self.x, self.y, color='red', label='Data Points')
        plt.title(plottitle)
        plt.xlabel(xtitle)
        plt.ylabel(ytitle)
        plt.legend()
        plt.grid(True)
        plt.show()


    def plotXY2(self, digramtitle, plottitle, xtitle, ytitle):

        plt.plot(self.x, self.y2, label=digramtitle)
        plt.scatter(self.x, self.y2, color='blue', label='Data Points')
        plt.title(plottitle)
        plt.xlabel(xtitle)
        plt.ylabel(ytitle)
        plt.legend()
        plt.grid(True)
        plt.show()


    def plotX2Y2(self, digramtitle, plottitle, xtitle, ytitle):

        plt.plot(self.x2, self.y2, label=digramtitle)
        plt.scatter(self.x2, self.y2, color='blue', label='Data Points')
        plt.title(plottitle)
        plt.xlabel(xtitle)
        plt.ylabel(ytitle)
        plt.legend()
        plt.grid(True)
        plt.show()