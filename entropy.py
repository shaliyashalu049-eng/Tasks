import numpy as np
import matplotlib.pyplot as plt

# Actual answer
y = 1

# Some predicted probabilities
y_pred = np.array([0.1, 0.2, 0.3, 0.4, 0.5,
                   0.6, 0.7, 0.8, 0.9])

# Calculate loss manually
loss = -np.log(y_pred)

# Display values
for p, l in zip(y_pred, loss):
    print(f"Prediction = {p:.1f}, Loss = {l:.3f}")

# Plot
plt.plot(y_pred, loss, marker='o')

plt.xlabel("Predicted Probability")
plt.ylabel("Cross-Entropy Loss")
plt.title("Cross-Entropy Loss for y = 1")

plt.grid()
plt.show()