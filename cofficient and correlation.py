x = [10, 20, 30, 40, 50]
y = [40, 30, 20, 10, 5]
x2 = [i * i for i in x]
y2 = [i * i for i in y]
n = len(x)
xy = [x[i] * y[i] for i in range(n)]

sigma_x = sum(x)
sigma_y = sum(y)
sigma_x2 = sum(x2)
sigma_y2 = sum(y2)  
sigma_xy = sum(xy)

b= (n *sigma_xy-sigma_x*sigma_y)/(n*sigma_x2-sigma_x**2)
a= (sigma_y-b*sigma_x)/n
r=(n*sigma_xy -sigma_x*sigma_y)/((n*sigma_x2-sigma_x**2)*(n*sigma_y2-sigma_y**2))**0.5

print("X", x, "Y", y, "x2", x2, "y2", y2, "XY", xy,)
print("sum of x:", sigma_x, "sum of y:", sigma_y, " sum of x2:", sigma_x2, "sum of y2:", sigma_y2, "sum of xy:", sigma_xy)
print("a =", a, "b =", b)
print("r =", r)