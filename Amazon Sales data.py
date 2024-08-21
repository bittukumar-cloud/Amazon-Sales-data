#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


data=pd.read_csv("D:\Sales Data.csv")
data.head()


# In[9]:


#convert 'order date' to datetime format
data['Order Date']=pd.to_datetime(data['Order Date'])


# In[13]:


# List of columns to sum
numeric_columns = data.select_dtypes(include=['number']).columns

#Total sales by month
monthly_sales=data.groupby('Month')[numeric_columns].sum()['Sales']

#Most popular products (by quantity sold)
popular_products = data.groupby('Product')[numeric_columns].sum()['Quantity Ordered'].sort_values(ascending=False)

#Sales by city
sales_by_city = data.groupby('City')[numeric_columns].sum()['Sales']

#Sales by hour (to find peak sales times)
sales_by_hour = data.groupby('Hour')[numeric_columns].sum()['Sales']
monthly_sales, popular_products.head(), sales_by_city, sales_by_hour


# In[14]:


# Set style for plots
sns.set(style="whitegrid")

# Monthly Sales Trends
plt.figure(figsize=(10, 6))
monthly_sales.plot(kind='line', marker='o', color='blue')
plt.title('Total Sales by Month')
plt.xlabel('Month')
plt.ylabel('Sales (in USD)')
plt.grid(True)
plt.xticks(range(1, 13))
plt.show()


# In[15]:


#Top 10 Best-Selling Products
plt.figure(figsize=(12, 6))
popular_products.head(10).plot(kind='bar', color='green')
plt.title('Top 10 Best-Selling Products')
plt.xlabel('Product')
plt.ylabel('Quantity Sold')
plt.xticks(rotation=45, ha='right')
plt.show()


# In[16]:


# Sales by City
plt.figure(figsize=(14, 7))
sales_by_city.sort_values().plot(kind='barh', color='purple')
plt.title('Total Sales by City')
plt.xlabel('Sales (in USD)')
plt.ylabel('City')
plt.show()


# In[17]:


# Sales by Hour
plt.figure(figsize=(10, 6))
sales_by_hour.plot(kind='line', marker='o', color='orange')
plt.title('Total Sales by Hour')
plt.xlabel('Hour of the Day')
plt.ylabel('Sales (in USD)')
plt.grid(True)
plt.xticks(range(0, 24))
plt.show()


# In[18]:


# Product Sales Distribution (Pie Chart)
plt.figure(figsize=(8, 8))
popular_products.head(10).plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Sales Among Top 10 Products')
plt.ylabel('')
plt.show()


# In[19]:


# Correlation Analysis (Heatmap)
plt.figure(figsize=(10, 8))
correlation_matrix = data[['Quantity Ordered', 'Price Each', 'Sales', 'Month', 'Hour']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of Sales Data')
plt.show()


# In[ ]:




