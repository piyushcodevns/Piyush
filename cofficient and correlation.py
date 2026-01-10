x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 4, 6]
x2 = [i * i for i in x]
y2 = [i * i for i in y]
n=len(x)
xy = [x[i]*y[i] for i in range(n)]

sigma_x=sum(x)
sigma_y=sum(y)
sigma_x2=sum(x2)
sigma_y2=sum(y2)
sigma_xy=sum(xy)

b=(n*sigma_xy-sigma_x*sigma_y)/(n*sigma_x2-sigma_x**2)
a=(sigma_y-b*sigma_x)/n
r=(n*sigma_xy-sigma_x*sigma_y)/((n*sigma_x2-sigma_x**2)*(n*sigma_y2-sigma_y**2))**0.5


print(f"{b:.2f}")
print(f"{a:.2f}")
print(f"{r:.2f}")