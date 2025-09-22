import matplotlib.pyplot as plt

overs = list(range(1, 21))
india_runs = [10, 30, 55, 75, 95, 120, 150, 170, 200, 220, 240, 260, 280, 300, 315, 330, 345, 355, 365, 370]
bangladesh_runs = [12, 28, 48, 70, 92, 118, 145, 165, 185, 210, 230, 250, 270, 290, 310, 325, 340, 355, 368, 375]

plt.plot(overs, india_runs, marker='o', linestyle='--', color='b', label="India")
plt.plot(overs, bangladesh_runs, marker='o', linestyle='--', color='orange', label="Bangladesh")
plt.xticks(range(1, 21))
plt.title("Cricket Match: India vs Bangladesh")
plt.xlabel("Overs")
plt.ylabel("Runs")
plt.legend()
plt.grid(True)
plt.show()