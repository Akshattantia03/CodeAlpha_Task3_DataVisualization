from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

workbook_path = Path(__file__).resolve().parents[2] / "Sample - Superstore_2024.xlsx"

df = pd.read_excel(
    workbook_path,
    sheet_name="Orders",
)

print(df.head())

print("Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nDataset Information:")
df.info()

missing_by_column = df.isna().sum()
print("\nMissing Values per Column:")
print(missing_by_column[missing_by_column > 0])
print(f"Total missing values: {missing_by_column.sum()}")

duplicate_count = df.duplicated().sum()
print(f"\nDuplicate rows: {duplicate_count}")
if duplicate_count > 0:
    print("Duplicate rows:")
    print(df[df.duplicated(keep=False)])

print("\nStatistical Summary:")
print(df.describe())

print("Minimum Order Date:", df["Order Date"].min())
print("Maximum Order Date:", df["Order Date"].max())

print(df["Category"].value_counts())
print(df["Region"].value_counts())

total_sales = df["Sales"].sum()

print("Total Sales:", total_sales)

total_profit = df["Profit"].sum()

print("Total Profit:", total_profit)
total_quantity = df["Quantity"].sum()

print("Total Quantity:", total_quantity)

total_orders = df["Order ID"].nunique()

print("Total Orders:", total_orders)

#analyze sales by category
category_sales = df.groupby("Category")["Sales"].sum()

print(category_sales)

# Matplotlib visualization

plt.figure(figsize=(8, 5))

plt.bar(
    category_sales.index,
    category_sales.values
)

plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.tight_layout()

plt.show()

plt.figure(figsize=(10, 6))

bars = plt.bar(
    category_sales.index,
    category_sales.values
)

plt.title(
    "Total Sales by Product Category",
    fontsize=16
)

plt.xlabel("Product Category")
plt.ylabel("Total Sales ($)")

plt.xticks(rotation=0)

plt.tight_layout()


plt.show()

plt.savefig(
    "../visualizations/sales_by_category.png",
    dpi=300,
    bbox_inches="tight"
)