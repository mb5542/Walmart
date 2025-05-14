# Walmart
Analysis of walmart shop sales data



**Data Cleaning & Preparation:**

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
  
__Data Analysis:__

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

1. _Sales by Gender:_
<img src="https://github.com/user-attachments/assets/335a8469-3f6c-406a-9161-37dc73e429a7" width="40%">

-Sales are fairly evenly distributed between genders, with slightly higher spending from customers identifying themselves as ‘Other’. This may suggest a diverse customer base and should be accounted in marketing strategies.

<br>

2. _Sales by age:_
   
**Minimum age:** 18

**Maximum age:** 60
| Age Group | Total Sales (USD) |
| --------- | ----------------- |
| 36–45     | 2,985,045.17      |
| 26–35     | 2,976,492.37      |
| 46–55     | 2,953,576.01      |
| 18–25     | 2,398,043.84      |
| 56–65     | 1,462,963.73      |

<img src="https://github.com/user-attachments/assets/6fbc3016-f7dd-4e5f-b86a-7d77ef83ecdc" width="40%">

<img src="https://github.com/user-attachments/assets/04c8dfef-4a48-4ef7-9875-6e92cdca49fd" width="40%">

**Interpretation:**
- The 36-45, 26-35, and 46-55 age groups generate the highest total sales - all above 2.9 million USD.
- These groups also have the largest customer base, suggesting strong purchasing behavior from middle-aged adults.
- The 56-65 age group has the lowest sales and smallest customer count, which may indicate either lower purchasing power.
- Younger adults (18-25) are also active, but spend slightly less overall.

**Recommendations:**
- Focus marketing efforts on the 26-55 age range with personalized offers.
- Consider tailored campaigns for older customers (e.g., senior discounts, pharmacy-related products, local flyer distribution).
- Develop engagement strategies for younger shoppers (e.g., mobile app offers, value bundles for students).

<br>

3. _Sales by city:_
   
**Total number of cities:** 25 095

Cities with the highest sales:

| Age Group | Total Sales (USD) |
| --------- | ----------------- |
| North Michael     | 11 478.75      |
| East Michael     | 10 866.51      |
| New Michael     | 10 574.68      |


<img src="https://github.com/user-attachments/assets/dd620d3f-812b-4f5e-9e27-985e49fe6bfe" width="40%">


Cities with the lowest sales:
| Age Group | Total Sales (USD) |
| --------- | ----------------- |
| Devintown      | 10.08      |
| West Melissaborough     | 10.08      |
| Port Karenfort     | 10.07      |


<img src="https://github.com/user-attachments/assets/b04e7d5f-6170-40b7-9641-e96a108afb40" width="40%">


**Interpretation:**
Very low sales (~10 USD) suggest minimal purchase activity, possibly due to: 
- Newly added regions,
- Or anomalies/test data in the dataset.

<br>

4. _Percentage of returning customers:_
         
**Percentage of returning customers:** 50.49%

This means that almost half of all customers in the dataset have made at least one additional purchase in the past - a strong indicator of repeat engagement.

**Important Data Note:**
Each customer ID appears only once in the dataset.
The information about return behavior is stored in a dedicated column, not based on repeated entries.

**Recommendations:**
Continue strengthening customer loyalty mechanisms:
- loyalty apps
- coupons
- targeted emails or mobile push notifications
     
      
