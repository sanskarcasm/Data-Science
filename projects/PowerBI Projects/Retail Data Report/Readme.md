Retail Sales Analysis with Power BI
📊 Project Overview
This project analyzes retail sales data using Power BI, focusing on uncovering sales trends, product and regional performance, and actionable business insights. The dashboard leverages DAX measures and interactive visuals to support data-driven decision-making.

🗂️ Data Description
Source: Kaggle - Sales Forecasting Dataset

Fields:

ORDER_ID, ORDER_DATE, SHIP_DATE, SHIP_MODE, CUSTOMER_ID, CUSTOMER_NAME, SEGMENT, COUNTRY, CITY, STATE, POSTAL_CODE, REGION, PRODUCT_ID, CATEGORY, SUB-CATEGORY, PRODUCT_NAME, SALES

Time Range: March 2015 – October 2028

🚦 Step-by-Step Process
Data Import: Connected Power BI to the Kaggle sales forecasting dataset and imported the DATA table.

Data Preparation:

Converted ORDER_DATE from text to date.

Created a Calendar table using DAX for time-based analysis.

Built relationships between DATA and Calendar.

DAX Measures:

Total Sales, Sales YTD, Last Year Sales, Sales Growth, etc.

Dashboard Design:

Line chart: Sales over time

Bar chart: Sales by product and region

Map: Sales by region

KPI cards: Total Sales, Sales Growth, etc.

Slicers: Year, Month, Quarter, Region, Category

Documentation & Export:

Exported key visuals as PNGs for this README.

Documented findings and DAX formulas.

🧮 Key DAX Formulas
text
Total Sales = SUM(DATA[SALES])

Sales YTD = TOTALYTD([Total Sales], Calendar[Date])

Last Year Sales = CALCULATE([Total Sales], SAMEPERIODLASTYEAR(Calendar[Date]))

Sales Growth = DIVIDE([Total Sales] - [Last Year Sales], [Last Year Sales])
📸 Dashboard Screenshots
Sales Over Time
![Sales Over Time](screenshots/sales-over-time.png Product

![Sales by Product](screenshots/sales by Region and Category

![Sales by Region](screenshots/sales Cards

![KPI Cards](screenshots/kpi-cards.png image paths above with your actual screenshot file paths._

📈 Insights & Outcomes
Sales Trends:
Sales increased steadily from 2015 to 2018, with the highest sales recorded in 2018. There is a clear upward trend in total sales year over year, indicating business growth and effective sales strategies.

Top-Selling Products:
Products such as the Canon imageCLASS, Fellowes PB500 Electric, and Cisco TelePresence Series were among the top performers, each generating substantial revenue.

Regional and Category Performance:
Sales were strong across all regions, with notable contributions from the Technology and Furniture categories. Office Supplies also maintained a consistent share of sales, though with room for growth.

Growth Rate:
The overall sales growth rate was positive, with a calculated growth of 68% over the period analyzed.

Seasonality:
Sales were distributed throughout the months and quarters, with some peaks in Q4, suggesting higher sales activity towards the end of the year.

Actionable Insights:

Focus marketing and inventory efforts on top-performing products and regions.

Leverage the end-of-year sales surge with targeted promotions.

Explore opportunities to boost Office Supplies category sales, which lag behind Technology and Furniture.

📝 How to Use
Open the .pbix file in Power BI Desktop.

Use slicers to filter by year, month, region, and category.

Interact with visuals for deeper insights.

📁 Files in this Repository
Retail-Sales-Analysis.pbix — Power BI report file

README.md — This documentation

screenshots/ — Folder containing exported PNGs of key visuals

sample-data.csv — (Optional) A sample of the underlying data (if allowed)

🌐 Project Link
Power BI Retail Sales Analysis on GitHub

💬 Connect
If you found this project useful, feel free to connect with me on LinkedIn and check out my other data science projects!

