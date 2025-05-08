# Walmart
Analysis of walmart shop sales data


**Data Cleaning & Preparation**
The dataset was preprocessed to ensure data quality and correct data types before analysis:
-  Loading: Imported from a semicolon-separated CSV file with Customer_ID as the index.

- Missing/invalid data:
Removed rows with missing Product_Name values.
Removed a corrupted row containing a non-numeric age value ("West Carolyn").

- Type conversions:
Purchase_Amount: Cleaned of $ symbols and converted to float.
Age: Converted to integer.
Purchase_Date: Converted to datetime.
Categorical columns (Gender, Category, Product_Name, Payment_Method, Repeat_Customer) were converted to category type.

- Final check: Verified column types and confirmed dataset integrity using .info()


__Data Analysis__
**Sales KPI Analysis – Insights**

1. Total sales
2. Average shopping basket
3. Average number of transactions per customer
4. Most popular products and categories
