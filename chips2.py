import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

# Load the entire datasets
purchase_data = pd.read_csv('C:\Users\utkarssh sehgal\Desktop\QVI_purchase_behaviour.csv')
transaction_data = pd.read_csv('C:\Users\utkarssh sehgal\Desktop\QVI_transaction_data.csv')

# Display first few rows of each dataset
print("Purchase Data:")
print(purchase_data.head())

print("\nTransaction Data:")
print(transaction_data.head())

# Merge datasets
merged_data = pd.merge(transaction_data, purchase_data, on='LYLTY_CARD_NBR', how='left')

# Check for missing values
print("\nMissing values in Merged Data:")
print(merged_data.isnull().sum())

# Outlier detection (using z-scores as an example)
outliers_tot_sales = merged_data[(np.abs(zscore(merged_data['TOT_SALES'])) > 3)]

# Feature engineering (example: derive pack size from a column)
merged_data['pack_size'] = merged_data['TOT_SALES'] / merged_data['PROD_QTY']

# Define metrics of interest

# 1. Customer Segmentation by LIFESTAGE and PREMIUM_CUSTOMER
customer_segments = merged_data.groupby(['LIFESTAGE', 'PREMIUM_CUSTOMER']).size().unstack()
print("\nCustomer Segmentation by LIFESTAGE and PREMIUM_CUSTOMER:")
print(customer_segments)

# 2. Spending Distribution by LIFESTAGE
plt.figure(figsize=(10, 6))
sns.boxplot(x='LIFESTAGE', y='TOT_SALES', data=merged_data)
plt.title('Spending Distribution by LIFESTAGE')
plt.xlabel('LIFESTAGE')
plt.ylabel('Spending')
plt.show()

# 3. Brand Preferences by LIFESTAGE
brand_preferences = merged_data.groupby(['LIFESTAGE', 'PROD_NAME'])['TOT_SALES'].mean().unstack()
print("\nBrand Preferences by LIFESTAGE:")
print(brand_preferences)

# 4. Top Selling Products
top_products = merged_data.groupby('PROD_NAME')['PROD_QTY'].sum().sort_values(ascending=False).head(10)
print("\nTop Selling Products:")
print(top_products)
