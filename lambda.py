import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sales data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = np.array([1200, 1500, 1800, 1700, 2100, 2500])

# Create a Pandas DataFrame
df = pd.DataFrame({
    "Month": months,
    "Sales": sales
})

# Display sales details
print("Sales Details")
print(df)

# Calculate statistics
print("\nTotal Sales:", df["Sales"].sum())
print("Average Sales:", df["Sales"].mean())
print("Maximum Sales:", df["Sales"].max())
print("Minimum Sales:", df["Sales"].min())

# Plot the sales data
plt.figure(figsize=(8, 5))
plt.plot(df["Month"], df["Sales"], marker="o", linewidth=2)
plt.title("Monthly Sales Report")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)

# Show the graph
plt.show()