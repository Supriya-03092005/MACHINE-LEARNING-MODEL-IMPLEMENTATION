import matplotlib.pyplot as plt

# -----------------------------
# SAMPLE DATA (House Size vs Price)
# -----------------------------
X = [500, 800, 1000, 1200, 1500, 1800, 2000]   # House size (sq ft)
Y = [150, 200, 230, 260, 300, 330, 360]       # Price (in thousands)

# -----------------------------
# LINEAR REGRESSION FROM SCRATCH
# -----------------------------
n = len(X)

mean_x = sum(X) / n
mean_y = sum(Y) / n

numerator = 0
denominator = 0

for i in range(n):
    numerator += (X[i] - mean_x) * (Y[i] - mean_y)
    denominator += (X[i] - mean_x) ** 2

m = numerator / denominator   # slope
c = mean_y - m * mean_x       # intercept

# -----------------------------
# PREDICTION
# -----------------------------
predicted_y = []
for x in X:
    predicted_y.append(m * x + c)

# -----------------------------
# VISUALIZATION
# -----------------------------
plt.scatter(X, Y)
plt.plot(X, predicted_y)
plt.xlabel("House Size (sq ft)")
plt.ylabel("House Price (in thousands)")
plt.title("Linear Regression Model Implementation")
plt.show()

# -----------------------------
# MODEL OUTPUT
# -----------------------------
print("Slope (m):", round(m, 2))
print("Intercept (c):", round(c, 2))

# Predict new value
new_size = 1600
predicted_price = m * new_size + c
print("Predicted price for 1600 sq ft house:", round(predicted_price, 2))
