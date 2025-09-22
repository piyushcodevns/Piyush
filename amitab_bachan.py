import matplotlib.pyplot as plt

flop = 0
hit = 1
superhit = 2
blockbuster = 3
allblockbuster = 4
x = list(range(1, 76))
y = [
    flop,
    flop,
    hit,
    flop,
    flop,
    flop,
    hit,
    flop,
    hit,
    flop,
    flop,
    flop,
    flop,
    superhit,
    flop,
    flop,
    hit,
    hit,
    superhit,
    flop,
    flop,
    blockbuster,
    hit,
    superhit,
    flop,
    blockbuster,
    flop,
    hit,
    hit,
    flop,
    hit,
    hit,
    superhit,
    hit,
    flop,
    allblockbuster,
    hit,
    superhit,
    superhit,
    hit,
    superhit,
    hit,
    flop,
    superhit,
    allblockbuster,
    blockbuster,
    flop,
    hit,
    flop,
    flop,
    superhit,
    flop,
    hit,
    hit,
    hit,
    blockbuster,
    hit,
    flop,
    superhit,
    flop,
    superhit,
    superhit,
    hit,
    hit,
    flop,
    hit,
    hit,
    superhit,
    hit,
    flop,
    blockbuster,
    flop,
    hit,
    hit,
    flop,
]


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
r = (n * sum_xy - sum_x * sum_y) / (
    (n * sum_x2 - sum_x * sum_x) * (n * sum_y2 - sum_y * sum_y)
) ** 0.5

yy=[i*b + a for i in x]

print(f"Regression Line: y = {b:.2f}x + {a:.2f}")
print(f"Correlation Coefficient (r): {r:.3f}")


# Plot graph
plt.scatter(x, y, color="blue")
plt.plot(x, y, color="lightblue")
plt.plot(x, yy, color="red", label="Regression Line")
plt.xlabel("Movie Number")
plt.ylabel("Performance")
plt.title("Movie Performance Graph")
plt.yticks(
    [0, 1, 2, 3, 4], ["Flop", "Hit", "Superhit", "Blockbuster", "All Blockbuster"]
)
plt.show()
