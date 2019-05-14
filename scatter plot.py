import numpy as np
import matplotlib.pyplot as plt
# Fixing random state for reproducibility
#x=np.linspace(0, 20, 10)

x=[3,5,10]
y=[2,6,7]
#N = 50

#colors = np.random.rand(N)
#area = (30 * np.random.rand(N))**2  # 0 to 15 point radii


plt.scatter(x, x**10)

plt.scatter(x,y)
plt.show()