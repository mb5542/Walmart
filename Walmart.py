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
