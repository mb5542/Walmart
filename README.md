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

---
  
__Data Analysis__
**Sales KPI Analysis – Insights**

1. Total sales:
   USD 12,776,121.12 over the entire analysis period (1 year).
- This indicates a high sales volume 

   
2. Average shopping basket:
   The average order value is USD 255.53
- It's suggesting that customers are purchasing relatively high-value items.

3. Average number of transactions per customer:
   On average, 1.00 transaction per customer.
- This suggests that most customers make a one-time purchase, potentially indicating opportunity to improve retention and remarketing efforts

4. Most popular products and categories:
 Top 3 most popular products:
Headphones    3261;
T-Shirt       3205;
Smartwatch    3177
-Their popularity may reflect current trends, effective promotions, or competitive pricing.

Most popular categories:
 Category
Electronics    12642;
Home           12492;
Beauty         12447;
Clothing       12417
-The distribution is very balanced, which suggests a diverse product offering and evenly spread customer interest.

**Recommendations:**
Consider introducing initiatives to increase customer loyalty (e.g., loyalty programs, newsletters, remarketing campaigns).
Strengthen marketing efforts around the most popular products and categories.

---

**Customer Segmentation – Insights**

1. Sales by Gender
<img src="https://github.com/user-attachments/assets/335a8469-3f6c-406a-9161-37dc73e429a7" width="40%">

-Sales are fairly evenly distributed between genders, with slightly higher spending from customers identifying themselves as ‘Other’. This may suggest a diverse customer base and should be accounted in marketing strategies.

