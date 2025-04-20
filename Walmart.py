# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 15:53:35 2025

@author: mb5542
"""

#Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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
1. Sales by gender
2. Sales by age
3. Sales by city
4. Percentage of returning customers
'''

# 1
# Sales by gender
sales_by_gender = walmart.groupby('Gender', observed=True)['Purchase_Amount'].sum().sort_values(ascending=False)
print(sales_by_gender)
print('\n')

plt.figure()
sales_by_gender.plot(kind='pie', title='Sales by gender', autopct="%.1f%%")
plt.show()

# 2
# Sales by age

# Age grouping
print('Min age: ', walmart['Age'].min())
print('Max age: ', walmart['Age'].max())
print('\n')

bins = [17,25,35,45,55,65]
labels = ['18-25','26-35','36-45','46-55','56-65']
walmart['Age_Group'] = pd.cut(walmart['Age'],bins=bins, labels=labels)

print(walmart['Age_Group'].value_counts())
print('\n')

sales_by_age = walmart.groupby('Age_Group', observed=True)['Purchase_Amount'].sum().sort_values(ascending=False)
print(sales_by_age)
print('\n')

plt.figure()
sales_by_age.plot(kind='bar', title='Sales by age')
plt.show()
#Age groups
walmart['Age_Group'].value_counts().plot(kind='bar', title='Size of age groups', color='y')

# 3 
# Sales by city
print(walmart['City'].nunique())

sales_by_city = walmart.groupby('City', observed=True)['Purchase_Amount'].sum()

#The three cities with the highest and the lowest sales
top_3_cities = sales_by_city.sort_values(ascending=False).head(3)
bottom_3_cities = sales_by_city.sort_values(ascending=False).tail(3)
print(top_3_cities)
print('\n')
print(bottom_3_cities)
print('\n')

# Comparison between cities
plt.figure()
top_3_cities.plot(kind='bar', title='Cities with the highest sales', color='g')
plt.ylim(3100, 12000) 
plt.show()

plt.figure()
bottom_3_cities.plot(kind='bar', title='Cities with the lowest sales', color='r')
plt.ylim(0, 12)
plt.show()

# 4. 
# Percentage of returning customers
repeat_customer = (walmart['Repeat_Customer']=='Yes').sum()
repeat_rate = repeat_customer/len(walmart['Repeat_Customer'])

print(f'Percentage of returning customers: {repeat_rate:.3f}%')

'''
Shopping basket analysis:
1. Most frequently purchased products
2. Top products by gender
3. Categories by gender
4. Average purchase amount by product category
'''

# 1
# Most frequently purchased products
top_5_products = walmart["Product_Name"].value_counts().head()
plt.figure()
top_5_products.plot(kind='bar', color='cornflowerblue', title='Best selling products')
plt.ylim(3100, 3300)
plt.show()

# 2
# Top products by gender
products_by_gender = walmart.groupby("Gender", observed=True)["Product_Name"].value_counts(normalize=True)
df_products = products_by_gender.reset_index(name='Share')
top3_by_gender = (df_products.groupby('Gender',observed=True).apply(lambda x: x.nlargest(3,'Share')).reset_index(drop=True))
print(f'Top 3 products by gender: \n{top3_by_gender}')
print('\n')

# 3
# Categories by gender:
categories_by_gender = walmart.groupby(["Gender","Category"],observed=True).size().unstack()
plt.figure()
sns.heatmap(categories_by_gender)
plt.title('Categories by gender')
plt.show()

# 4
# Average purchase amount by product category
avg_purchase_by_category = walmart.groupby("Category", observed=True)['Purchase_Amount'].mean().sort_values(ascending=False)

plt.figure()
avg_purchase_by_category.plot(kind='bar', color='teal', title='Average purchase amount by product category')
plt.ylim(245, 260)
plt.show()


'''
Payments:
1. Share of payment methods
2. Impact of Payment Method on Spend
3. Impact of discounts on average rating
'''

# 1
# Share of payment methods
payment_share = walmart['Payment_Method'].value_counts(normalize=True)

plt.figure()
payment_share.plot(kind='pie', autopct='%.1f%%', title='Share of payment methods')
plt.show()

# 2
# Impact of Payment Method on Spend

avg_spend_by_payment = walmart.groupby('Payment_Method', observed=True)['Purchase_Amount'].mean().sort_values(ascending=True)

plt.figure()
avg_spend_by_payment.plot(kind='bar', title='Average spend by payment', color='skyblue')
plt.ylim(250, 258)
plt.show()



# Anova test
from scipy.stats import f_oneway

groups_payment = [group['Purchase_Amount'].values for name, group in walmart.groupby('Payment_Method', observed=True)]

anova_payment_result = f_oneway(*groups_payment)
print('\nAnova test for payment methods')
print('F statistics:', anova_payment_result.statistic)
print("P-value:", anova_payment_result.pvalue)
print('\n')
if anova_payment_result.pvalue < 0.05:
    print('We reject the null hypothesis - the differences are statistically significant.')
else:
    print('No grounds to reject the null hypothesis - differences are not significant.')
print('\n')    
    
# 3 
# Impact of discounts on average rating

avg_rating_by_discounts = walmart.groupby('Discount_Applied', observed=True)['Rating'].mean()
print(f'Average rating by discounts:\n {avg_rating_by_discounts.round(3)}')

# t-student test
from scipy import stats

group_yes = walmart[walmart['Discount_Applied'] == 'Yes']['Rating']
group_no = walmart[walmart['Discount_Applied'] == 'No']['Rating']

t_stat, p_value = stats.ttest_ind(group_yes,group_no)
print("\nStudent's t-test for discounts")
print(f'T-statistic: {t_stat}')
print(f'P-value: {p_value}')
print('\n')

if p_value < 0.05:
    print('We reject the null hypothesis - the differences are statistically significant.')
else:
    print('No grounds to reject the null hypothesis - differences are not significant.')
print('\n')  
    
  
'''
Seasonality and trend analysis:
1. Sales by time (daily/monthly)
2. Best/worst-performing days of the week
3. Average order value by date
'''

# 1
# Sales by time (daily/monthly)
daily_sales = walmart.groupby('Purchase_Date', observed=True)['Purchase_Amount'].sum()

plt.figure()
daily_sales.plot(title='Daily sales') 
plt.show()

# Mothly sales

walmart['Month'] = walmart['Purchase_Date'].dt.to_period('M')
monthly_sales = walmart.groupby('Month', observed=True)['Purchase_Amount'].sum()

plt.figure()
monthly_sales.plot(title='Mothly sales') 
plt.show()

print(walmart['Purchase_Date'].min())
print(walmart['Purchase_Date'].max())
# Skip February - no data for whole months
month_filter = walmart[~walmart['Month'].isin([pd.Period("2024-02"),pd.Period('2025-02')])]

monthly_sales_filtered = month_filter.groupby('Month', observed=True)['Purchase_Amount'].sum()

plt.figure()
monthly_sales_filtered.plot(title='Mothly sales') 
plt.show()

