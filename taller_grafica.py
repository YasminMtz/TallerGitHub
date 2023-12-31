import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery-nogrid')

# make data: correlated + noise
np.random.seed(1)
x = np.random.randn(5000)
y = 1.2 * x + np.random.randn(5000) / 3
#cambiossss
# plot:
fig, ax = plt.subplots()
#otro comentario dos 
ax.hexbin(x, y, gridsize=20)
plt.xlabel('Eje de las x')
plt.ylabel('Eje de las x')
ax.set(xlim=(-2, 2), ylim=(-3, 3))

plt.show()
