import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure();
ax = fig.add_subplot(1, 1, 1, projection='polar');

theta1 = [0, 0.5*np.pi, 0, 0];
r1 = [1, 1, 0, 1];

ax.plot(theta1, r1, color='r');

plt.show();