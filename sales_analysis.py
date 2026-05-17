# =====================================================
# SALES DATA ANALYSIS PROJECT
# Synent Technologies Internship - Task 5
# =====================================================

# ---------- IMPORT LIBRARIES ----------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("\n========== IMPORTS SUCCESSFUL ==========")

# =====================================================
# LOAD DATASET
# =====================================================

print("\nLoading Dataset...")

df = pd.read_csv("Sample - Superstore.csv", encoding='latin1')

print("Dataset Loaded Successfully!")

# =====================================================
# BASIC DATASET INFORMATION
# =====================================================

print("\n========== DATASET OVERVIEW ==========")

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

# =====================================================
# DATA CLEANING
# =====================================================

print("\n========== DATA CLEANING ==========")

duplicates = df.duplicated().sum()

print(f"Duplicate Rows Found: {duplicates}")

df.drop_duplicates(inplace=True)

print("Duplicate Rows Removed Successfully!")

# Convert date columns
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Create Month-Year column
df['Month_Year'] = df['Order Date'].dt.to_period('M')

print("Date Conversion Completed!")

print("\nCleaned Dataset Shape:")
print(df.shape)

# =====================================================
# SUMMARY STATISTICS
# =====================================================

print("\n========== SUMMARY STATISTICS ==========")

print(df.describe())

# =====================================================
# KPI ANALYSIS
# =====================================================

print("\n========== KPI ANALYSIS ==========")

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_orders = df['Order ID'].nunique()
avg_profit = df['Profit'].mean()

print(f"Total Sales: {total_sales:.2f}")
print(f"Total Profit: {total_profit:.2f}")
print(f"Total Orders: {total_orders}")
print(f"Average Profit: {avg_profit:.2f}")

# =====================================================
# VISUALIZATION FUNCTION
# =====================================================

def show_plot():
    plt.tight_layout()
    plt.show(block=False)
    plt.pause(2)
    plt.close()

# =====================================================
# MONTHLY REVENUE TREND
# =====================================================

print("\nGenerating Monthly Revenue Trend Graph...")

monthly_sales = df.groupby('Month_Year')['Sales'].sum()

plt.figure(figsize=(14,6))

monthly_sales.plot()

plt.title("Monthly Revenue Trend")
plt.xlabel("Month-Year")
plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.grid(True)

show_plot()

print("Monthly Revenue Trend Graph Completed!")

# =====================================================
# TOP SELLING PRODUCTS
# =====================================================

print("\nGenerating Top Selling Products Graph...")

top_products = df.groupby('Product Name')['Sales'] \
                 .sum() \
                 .sort_values(ascending=False) \
                 .head(10)

plt.figure(figsize=(12,6))

sns.barplot(
    x=top_products.values,
    y=top_products.index
)

plt.title("Top 10 Selling Products")
plt.xlabel("Sales")
plt.ylabel("Product Name")

show_plot()

print("Top Selling Products Graph Completed!")

# =====================================================
# CATEGORY-WISE SALES
# =====================================================

print("\nGenerating Category-wise Sales Chart...")

category_sales = df.groupby('Category')['Sales'].sum()

plt.figure(figsize=(8,5))

plt.pie(
    category_sales.values,
    labels=category_sales.index,
    autopct='%1.1f%%'
)

plt.title("Category-wise Sales Distribution")

show_plot()

print("Category-wise Sales Chart Completed!")

# =====================================================
# REGION-WISE PROFIT ANALYSIS
# =====================================================

print("\nGenerating Region-wise Profit Analysis Graph...")

region_profit = df.groupby('Region')['Profit'].sum()

plt.figure(figsize=(8,5))

sns.barplot(
    x=region_profit.index,
    y=region_profit.values
)

plt.title("Region-wise Profit Analysis")
plt.xlabel("Region")
plt.ylabel("Profit")

show_plot()

print("Region-wise Profit Analysis Graph Completed!")

# =====================================================
# SHIP MODE ANALYSIS
# =====================================================

print("\nGenerating Ship Mode Analysis Graph...")

ship_mode_sales = df.groupby('Ship Mode')['Sales'].sum()

plt.figure(figsize=(8,5))

sns.barplot(
    x=ship_mode_sales.index,
    y=ship_mode_sales.values
)

plt.title("Sales by Ship Mode")
plt.xlabel("Ship Mode")
plt.ylabel("Sales")

plt.xticks(rotation=15)

show_plot()

print("Ship Mode Analysis Graph Completed!")

# =====================================================
# SEGMENT ANALYSIS
# =====================================================

print("\nGenerating Customer Segment Analysis Graph...")

segment_sales = df.groupby('Segment')['Sales'].sum()

plt.figure(figsize=(8,5))

sns.barplot(
    x=segment_sales.index,
    y=segment_sales.values
)

plt.title("Customer Segment Sales")
plt.xlabel("Segment")
plt.ylabel("Sales")

show_plot()

print("Customer Segment Analysis Graph Completed!")

# =====================================================
# PROFIT VS SALES SCATTER PLOT
# =====================================================

print("\nGenerating Profit vs Sales Scatter Plot...")

plt.figure(figsize=(10,6))

sns.scatterplot(
    x='Sales',
    y='Profit',
    hue='Category',
    data=df
)

plt.title("Profit vs Sales")
plt.xlabel("Sales")
plt.ylabel("Profit")

show_plot()

print("Profit vs Sales Scatter Plot Completed!")

# =====================================================
# CORRELATION HEATMAP
# =====================================================

print("\nGenerating Correlation Heatmap...")

numeric_df = df.select_dtypes(include=np.number)

plt.figure(figsize=(8,5))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Heatmap")

show_plot()

print("Correlation Heatmap Completed!")

# =====================================================
# BUSINESS INSIGHTS
# =====================================================

print("\n========== BUSINESS INSIGHTS ==========")

print("1. Technology category contributes high sales.")

print("2. Some regions generate higher profits than others.")

print("3. Monthly revenue shows seasonal growth trends.")

print("4. Certain products dominate overall sales.")

print("5. Higher sales do not always mean higher profit.")

# =====================================================
# PROJECT SUMMARY
# =====================================================

print("\n========== PROJECT SUMMARY ==========")

print(f"Dataset Size: {df.shape}")

print(f"Total Sales: {total_sales:.2f}")

print(f"Total Profit: {total_profit:.2f}")

print(f"Total Orders: {total_orders}")

# =====================================================
# FINAL TERMINATION
# =====================================================

print("\n======================================")
print("PROJECT EXECUTED SUCCESSFULLY!")
print("Sales Data Analysis Completed.")
print("Program Terminated Successfully.")
print("======================================")