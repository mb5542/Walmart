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

<br>

---

**Shopping basket analysis:**

1. _Most frequently purchased products_

<img src="https://github.com/user-attachments/assets/46cd094d-8f9e-40ed-80c3-1bde64a3a069" width="40%">

**Interpretation:**
- The top products span multiple categories, including electronics, clothing, personal care, and home goods — reflecting the diverse shopping behavior of Walmart customers.
- Products like headphones and smartwatches suggest strong demand in affordable tech.
- Face cream points to consistent interest in beauty/personal care — likely repeat-purchased items.
- T-shirts and sofa covers indicate a blend of everyday apparel and home essentials, both of which align with Walmart’s core retail offering.

**Recommendations:**
- Ensure optimal inventory levels for these products to avoid out-of-stock scenarios.
- Consider bundling strategies — e.g., pair headphones with chargers

<br>

2. _Top products by gender:_

| Gender | Product    | Share (%) |
| ------ | ---------- | --------- |
| Female | T-Shirt    | 6.59%     |
| Female | Jacket     | 6.56%     |
| Female | Headphones | 6.52%     |
| Male   | Headphones | 6.65%     |
| Male   | Laptop     | 6.52%     |
| Male   | Face Cream | 6.49%     |
| Other  | Smartwatch | 6.72%     |
| Other  | Curtains   | 6.47%     |
| Other  | Smartphone | 6.44%     |

**Interpretation:**
- Female customers prefer a mix of clothing (T-shirts, jackets) and electronics (headphones).
- Male customers favor technology products (headphones, laptops) but also show interest in personal care (face cream).
- Customers categorized as Other gravitate toward tech and home products (smartwatches, curtains, smartphones)
In summary, clothing dominates among women, while tech items such as laptops and smartphones are more popular among men and others.

**Recommendations:**
- Promote clothing deals to female customers.
- Emphasize tech bundles or upgrades for male and Other genders.

<br>

3. _Categories by gender:_
   
<img src="https://github.com/user-attachments/assets/31ba593f-dde1-441e-8699-e4b9e1a4577a" width="40%">

**Interpretation:**

- Male shoppers show a clear preference for Electronics, and relatively lower interest in Clothing.
- Female shoppers demonstrate a more balanced distribution across all categories, though Electronics is still the lowest for them.
- Other gender group leads in both Electronics and Clothing, suggesting this segment engages broadly in both tech and apparel.

**Recommendations:**

Consider gender-based category promotions:
- Electronics for Male and Other.
- Clothing and Home for Female and Other.

<br>

4. _Average purchase amount by product category:_

<img src="https://github.com/user-attachments/assets/d9e5795d-ec0f-49cc-acb5-530641fa2035" width="40%">


**Interpretation:**
- The top position for electronics is expected due to typically more expensive
- The small gap between categories may suggest that Walmart maintains competitive pricing even in categories often considered luxury or non-essential
- Clothing, which has the lowest average, consist of cheaper, frequent purchases such as T-shirts and basic clothing.

**Recommendations**
- Upsell or bundle offers can be introduced in Clothing to raise the average purchase amount.
- Highlight premium items in the Home and Beauty sections to potentially match Electronics’ revenue contribution.

<br>

---

**Payments:**

_1. Share of payment methods:_

<img src="https://github.com/user-attachments/assets/e04758f2-c103-48bd-b09b-a32d3495ecd7" width="40%">

**Interpretation:**
- This almost equal split indicates that Walmart has successfully integrated multiple payment options, offering flexibility
- The small differences in usage suggest that consumer preferences are diverse and no single method dominates

**Recommendations**
- Maintain support for all current payment methods, as each supports a significant proportion of the customer base.
- Promote digital methods (e.g. UPI, cards) through incentives (e.g. cashback, loyalty points) to gradually move away from cash - reducing handling costs and fraud risk.

<br>

_2. Impact of Payment Method on Spend_

<img src="https://github.com/user-attachments/assets/83b90822-8c1c-4cbb-ba5d-146edaa6f9c6" width="40%">

Anova test for payment methods:

F statistics: 0.1980970383845948

P-value: 0.8977374886444247

**Interpretation:**
- At first glance, the average spend appears slightly higher for UPI and Cash on Delivery, but the differences are marginal — within about $1.30 across all methods.
- The P-value (0.898) is far above the common significance level (0.05), meaning there's no statistically significant difference in purchase amounts across payment methods.
- In other words, how customers pay does not influence how much they spend.

**Recommendations**
- Maintain support for all payment types, as they perform similarly in terms of customer spend.
- Focus on user experience and transaction success rate, rather than trying to steer users toward "higher spending" methods, since no real impact exists.

<br>

_3. Impact of discounts on average rating:_

| Discount Applied | Average Rating |
| ---------------- | -------------- |
| No           | 3.000     |
| Yes          | 2.997          |

Student's t-test for discounts:

T-statistic: -0.20199103434680427

P-value: 0.8399245551082193

**Interpretation:**
- The difference in average ratings is minimal (0.003 points), suggesting that discounts do not meaningfully affect how customers rate their purchases.
- The P-value is much higher than the typical threshold of 0.05.
- This means we fail to reject the null hypothesis: there is no significant difference in average ratings between discounted and non-discounted purchases.

**Recommendations**
- Discounts can be used to drive sales or clear inventory without concern that they will lower customer satisfaction.
- Marketing strategies can focus on the transactional or volume benefits of discounts rather than trying to improve ratings through them.

<br>

---

**Seasonality and trend analysis:**

_1. Sales by time (daily/monthly)_

<img src="https://github.com/user-attachments/assets/07930891-402f-434a-919a-ce7f05475b86" width="40%">

**Interpretation:**
- The daily sales chart shows significant day-to-day fluctuations, with purchase amounts typically ranging between 27,000 and 43,000. 
- No clear seasonality is observed. 
- The peaks and dips appear to be random

<img src="https://github.com/user-attachments/assets/aabf0ff1-b8ae-4ee9-935d-8c912dce25ab" width="40%">

**Interpretation:**
- There is a steep increase in sales from February to March 2024 due to incomplete data for February. 
- From March 2024 to January 2025, total monthly sales are very consistent, ranging around 1.05 to 1.10 million. 
- February 2025 again shows a drop due to partial month data.

To better see the differences between the months, February 2024 and 2025 have been omitted

<img src="https://github.com/user-attachments/assets/fdfbe472-822d-4a9e-a999-d1f4043f0e64" width="40%">

**Interpretation:**
- After filtering out incomplete months, the sales across March 2024 to January 2025 are relatively steady, with small natural fluctuations. 
- No single month stands out as significantly better or worse, indicating a well-balanced sales performance throughout the year.

<br>

_2. Best performing day of the week_

<img src="https://github.com/user-attachments/assets/11eb7ecb-70e3-4ca8-b150-7eadda67c061" width="40%">

