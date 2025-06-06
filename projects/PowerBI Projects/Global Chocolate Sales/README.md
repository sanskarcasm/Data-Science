Global Chocolate Sales Dashboard – Power BI
📊 Project Overview
This project delivers an executive-level Power BI dashboard visualizing 12 months of global chocolate sales across 5 regions. The report supports over 10 key performance indicators (KPIs), enabling business leaders to monitor trends, compare multi-year performance, and drill down into product category insights. By leveraging advanced DAX and interactive filtering, the solution reduced manual reporting time by 50% and empowered data-driven decision-making.

🗂️ Data Description
Dataset: 12 months of chocolate sales data (global, multi-region)

Regions Covered: Australia, Canada, UK, India, USA, New Zealand

Sample Fields:

Date (Year, Quarter, Month)

Country/Region

Product Name & Category

Boxes Shipped

Sales Amount

🚦 Process & Features
Data Modeling:

Cleaned and structured sales data for robust analysis.

Created date and product dimension tables for flexible reporting.

Advanced DAX Calculations:

Built dynamic measures for YTD, QTD, MTD, prior year comparisons, and growth rates.

Enabled complex filtering and custom KPI calculations.

Interactive Dashboard Design:

Visuals: Line charts (sales over time), bar charts (by product/region), maps (regional sales), and KPI cards.

Drill-down capability for product categories and time periods.

Slicers for region, product, and date to allow executive-level interactivity.

Performance & Efficiency:

Automated recurring reports, reducing manual reporting time by 50%.

Optimized DAX queries for fast, responsive dashboards.

🧮 Key DAX Examples
text
Total Sales = SUM(Sales[Amount])

Sales YTD = TOTALYTD([Total Sales], Dates[Date])

Sales Growth % = DIVIDE([Total Sales] - [Last Year Sales], [Last Year Sales])

Boxes Shipped = SUM(Sales[Boxes Shipped])
📈 Outcomes & Insights
Sales Performance:
Identified monthly and quarterly sales trends across all regions, with clear seasonal peaks and growth opportunities.

Top Products:
Highlighted best-selling chocolate products, such as Milk Bars, 85% Dark Bars, and After Nines.

Regional Insights:
Mapped and compared sales volumes and revenue across Australia, Canada, UK, India, USA, and New Zealand.

Efficiency Gains:
Reduced manual reporting time by 50% through automation and self-service analytics.

Executive Value:
Delivered actionable insights on category performance, enabling targeted marketing and supply chain decisions.

🛠️ Tools & Skills Used
Power BI Desktop: Data modeling, visualization, and dashboard creation.

DAX: Advanced measures, time intelligence, dynamic filtering.

SQL: Data preparation and transformation (if applicable).

Data Visualization: Executive dashboards, drill-downs, and interactivity.

Documentation & Reporting: Automated exports and reporting for stakeholders.

📁 Files in this Repository
Chocolate-Sales-Dashboard.pbix — Power BI report file

README.md — This documentation

screenshots/ — Exported visuals for quick reference

sample-data.csv — (Optional) Sample anonymized data

📄 How to Use
Download and open the .pbix file in Power BI Desktop.

Use slicers to filter by date, region, or product.

Click visuals to drill down into specific categories or time periods.

Export insights or visuals as needed for presentations and reports.

🌐 Connect
For feedback, collaboration, or to see more projects, connect with me on LinkedIn.https://www.linkedin.com/in/sanskar-pant-44b3801ab/

If you need further customization or want to add links to your dataset or live dashboard, just let me know!

