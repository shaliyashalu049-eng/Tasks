import numpy as np
import matplotlib.pyplot as plt

# Input logits
z = np.array([2.0, 1.0, 0.5])

# Softmax function
exp_z = np.exp(z)
softmax = exp_z / np.sum(exp_z)

print("Logits:", z)
print("Softmax probabilities:", softmax)
print("Sum of probabilities:", np.sum(softmax))

# Softmax gradient / Jacobian
J = np.diag(softmax) - np.outer(softmax, softmax)

print("\nSoftmax Jacobian:")
print(J)

# Visualize probabilities
classes = ["Class 1", "Class 2", "Class 3"]

plt.bar(classes, softmax)
plt.xlabel("Classes")
plt.ylabel("Probability")
plt.title("Softmax Probabilities")
plt.ylim(0, 1)
plt.grid(axis="y")
plt.show()

# Visualize Jacobian
plt.imshow(J)
plt.colorbar()
plt.xticks(range(3), classes)
plt.yticks(range(3), classes)
plt.xlabel("Input logits")
plt.ylabel("Output probabilities")
plt.title("Softmax Jacobian")
plt.show()