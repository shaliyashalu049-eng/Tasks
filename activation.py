import numpy as np
import matplotlib.pyplot as plt

z = np.linspace(-5, 5, 100)
# ReLU
#relu = np.maximum(0, z)
# ReLU gradient
#gradient = np.where(z > 0, 1, 0)

# Tanh
#tanh = np.tanh(z)

# Tanh gradient
#gradient = 1 - tanh**2

#subplot
plt.subplot(1, 2, 1)
#plt.plot(z, relu)
#plt.plot(z, tanh)
plt.xlabel("z")
plt.ylabel("z")
plt.title("Activation Function")
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(z, gradient)
plt.xlabel("z")
plt.ylabel("Gradient")
plt.title("Gradient")
plt.grid()

plt.tight_layout()
plt.show()