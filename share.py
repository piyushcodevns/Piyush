x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
x2 = [i * i for i in x]
y2 = [i * i for i in y]
n = len(x)
xy = [x[i] * y[i] for i in range(n)]
sum_x = sum(x)
sum_y = sum(y)
sum_x2 = sum(x2)
sum_y2 = sum(y2)
sum_xy = sum(xy)
b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x)
a = (sum_y - b * sum_x) / n
print("a=", a)
print("b=", b)

import matplotlib.pyplot as plt
plt.plot(x,y,label='Original data',color='blue')
plt.scatter(x,y,label='Fitted line',color='red')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
plt.legend()
plt.show()