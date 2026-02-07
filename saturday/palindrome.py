import matplotlib.pyplot as plt
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug']
sales = [120, 130, 115, 150, 170, 165, 180, 190]
plt.plot(months,sales)
plt.scatter(months,sales,color='black')
plt.colorbar()
plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Monthly Sales Data')
plt.show()