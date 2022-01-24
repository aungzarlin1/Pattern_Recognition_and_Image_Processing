import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 200)
print(x)
plt.plot(x, np.sin(x))
plt.show()