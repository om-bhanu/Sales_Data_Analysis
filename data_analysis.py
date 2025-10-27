import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load CSV file
data = pd.read_csv("sales_data.csv")

# Step 2: Show first 5 rows
print(" First 5 rows of data:")
print(data.head())

# Step 3: Basic info
print("\n📋 Data Info:")
print(data.info())

# Step 4: Total sales by product
print("\n Total Sales by Product:")
print(data.groupby("Product")["Sales"].sum())

# Step 5: Total profit by region
print("\n📈 Total Profit by Region:")
print(data.groupby("Region")["Profit"].sum())

# Step 6: Plot total sales by product
data.groupby("Product")["Sales"].sum().plot(kind="bar", color="skyblue", title="Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# Step 7: Plot profit by region
data.groupby("Region")["Profit"].sum().plot(kind="bar", color="orange", title="Total Profit by Region")
plt.xlabel("Region")
plt.ylabel("Total Profit")
plt.tight_layout()
plt.show()

# Step 8: Shape and NaN check
print("\n Shape of DataFrame:", data.shape)
print("\n Missing Values (NaN):")
print(data.isnull().sum())
