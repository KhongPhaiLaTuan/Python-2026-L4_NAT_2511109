import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-5, 5, 10)
y = 2*x + np.sin(x)**2 + 3

plt.plot(x, y, marker="s", label="y = 2x + sin^2(x) + 3")

plt.title("hello, po")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.savefig("labwork_6/po.pdf", dpi=300)
plt.show
