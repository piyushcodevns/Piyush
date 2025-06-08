import matplotlib.pyplot as plt

def makeFilledGraph(x, y, title):
    plt.plot(x, y, color="orange", linewidth=2, label="Data Line") 
    plt.fill_between(x, y, color="yellow", alpha=0.3) 
    plt.title(title)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True, alpha=0.5)
    plt.legend()
    plt.show()

x = [1, 2, 3, 4, 5, 6, 7]
y = [31, 33, 33, 30, 27, 26, 24]

print()
makeFilledGraph(x, y, "Filled Graph Example")