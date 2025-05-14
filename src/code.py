import pandas as pd

df = pd.read_csv("../data/laptop_price - dataset.csv")

# Calculate skewness of a numerical column, e.g., Price
print("Skewness of Price:", df["Price (Euro)"].skew())

import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
plt.hist(df["Price (Euro)"], bins=30, color="skyblue", edgecolor="black")
plt.title("Distribution of Laptop Prices")
plt.xlabel("Price (Euro)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
