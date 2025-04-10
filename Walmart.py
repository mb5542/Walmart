# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 15:53:35 2025

@author: mb5542
"""

#Import libraries
import pandas as pd
import numpy as np
import matplotlib as plt

# Import dataset
walmart = pd.read_csv(r'd:\programy\python312\scripts\Walmart\Walmart_customer_purchases.csv')

# Quick data check
print(walmart.head())
print('\n')

#Import csv file with semicolon as separator
walmart = pd.read_csv(r'd:\programy\python312\scripts\Walmart\Walmart_customer_purchases.csv', sep=';', index_col='Customer_ID')

# Quick data check
print(walmart.head())
print('\n')
print(walmart.tail())
print('\n')


# Info about dataset
print(walmart.info())
print('\n')

'''
Conclusions:
1. Only Product_Name has one not-null value
2. Purchase_amount and Age may need to be changed to a numerical type 
3. Purchase_date may need to be changed to a 'datatime' type
4. Gender, Category, Product_Name, Payment_Method can be changed to a 'category' type
'''

# 1.
print(walmart.loc[walmart['Product_Name'].isnull()])
print('\n')
# Both rows contain invalid values in the columns and should be deleted

#Delete invalid rows
walmart = walmart.dropna(subset='Product_Name')
print(walmart.info())
print('\n')

# 2.
# Check column content
print(walmart['Purchase_Amount'].value_counts())
print('\n')
# The number is concatenated with the $ symbol so this data type is not numeric

# Delete $ symbol 
walmart['Purchase_Amount']=walmart['Purchase_Amount'].str.replace('$',"")

# Change data type
walmart['Purchase_Amount'] = walmart['Purchase_Amount'].astype('float')
print(walmart['Purchase_Amount'].head())
print('\n')

# Check column content
print(walmart['Age'].value_counts())
print('\n')
# This column contains inappriopriete value 'West Carolyn'

# pd.set_option('display.max_columns',6)
print(walmart.loc[walmart['Age']=='West Carolyn'])
print('\n')
# The entire row is messed up

#Delete invalid row
walmart = walmart.loc[walmart['Age']!='West Carolyn']
print(walmart['Age'].value_counts())
print('\n')

# Change data type
walmart['Age'] = walmart['Age'].astype('int')
print(walmart['Age'].head())
print('\n')

print(walmart.info())
print('\n')

# 3.
# Check column content
print(walmart['Purchase_Date'].value_counts())

# Change data type
walmart['Purchase_Date'] = pd.to_datetime(walmart['Purchase_Date'])
print(walmart['Purchase_Date'].head())

print(walmart.info())
print('\n')

# 4
# Check column content and change data type of the Gender, Category, Product_Name, Payment_Method, Repeat_Customer columns
print(walmart['Gender'].value_counts())
walmart['Gender'] = walmart['Gender'].astype('category')

print(walmart['Category'].value_counts())
walmart['Category'] = walmart['Category'].astype('category')

print(walmart['Product_Name'].value_counts())
walmart['Product_Name'] = walmart['Product_Name'].astype('category')

print(walmart['Payment_Method'].value_counts())
walmart['Payment_Method'] = walmart['Payment_Method'].astype('category')

print(walmart['Repeat_Customer'].value_counts())
walmart['Repeat_Customer'] = walmart['Repeat_Customer'].astype('category')
print('\n')

# Check column types after changes
print(walmart.info())

print('\n')
print(walmart.head())
print('\n')


'''
Sales KPI analysis:
1. Total sales
2. Average shopping basket
3. Average number of transactions per customer
4. Most popular products and categories
'''
print('Sales KPIs:')
print('\n')
# 1
# Total sales
total_sales = walmart['Purchase_Amount'].sum()

print(f'Total sales: {total_sales:.2f} USD')

# 2
# Average shopping basket
avg_basket = walmart['Purchase_Amount'].mean()

print(f'Average shopping basket: {avg_basket:.2f} USD')

# 3
# Average number of transactions per customer

# Number of transactions per customer
trans_per_customer = walmart.groupby(walmart.index).size()

# Average number of transactions per customer
avg_transactions = trans_per_customer.mean()

print(f"Average number of transactions per customer: {avg_transactions:.2f}")
print('\n')

# 4
# Most popular products and categories

#Product popularity
product_popularity = walmart['Product_Name'].value_counts().sort_values(ascending=False)

print("Most popular products:\n", product_popularity)
print('\n')

# Category popularity
category_popularity = walmart['Category'].value_counts().sort_values(ascending=False)

print("Most popular categories:\n", category_popularity)
print('\n')

'''
Customer segmentation:
1. Sales by gender, age group, city?
2. Percentage of returning customers
3. Average order value in different customer groups
'''

# 1
# a) Sales by gender
sales_by_gender = walmart.groupby('Gender', observed=True)['Purchase_Amount'].sum().sort_values(ascending=False)
print(sales_by_gender)

sales_by_gender.plot(kind='pie', title='Sales by gender', autopct="%.0f%%")

# Group Age
# print(walmart['Age'].min())
# print(walmart['Age'].max())


