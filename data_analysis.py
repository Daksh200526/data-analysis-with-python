# data_analysis_project.py

import pandas as pd
import matplotlib.pyplot as plt

# Load multiple datasets
df_sales = pd.read_csv("sales_data.csv")
df_customers = pd.read_csv("customer_data.csv")

# Basic Cleaning
df_sales.dropna(inplace=True)
df_customers.drop_duplicates(inplace=True)

# Merge datasets on 'CustomerID'
df = pd.merge(df_sales, df_customers, on='CustomerID')

# Transform: Create TotalPrice column
df['TotalPrice'] = df['Quantity'] * df['Price']

# Analysis: Top 5 customers by total spending
top_customers = df.groupby('CustomerName')['TotalPrice'].sum().sort_values(ascending=False).head(5)

# Visualization
plt.figure(figsize=(10, 6))
top_customers.plot(kind='bar', color='skyblue')
plt.title('Top 5 Customers by Spending')
plt.ylabel('Total Spending')
plt.xlabel('Customer Name')
plt.tight_layout()
plt.show()
