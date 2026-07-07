use sales_db;

-- total records
select count(*) as total_records
from sales_data;

-- total sales
select sum(Sales) as total_Sales
from sales_data;

-- total profit
select sum(Profit) as total_profit
from sales_data;

-- average sales
select avg(Sales) as average_Sales
from sales_data;

-- Business Analysis Queries

-- sales by category
select Category, sum(Sales) as Total_Sales
from sales_data
group by Category
order by Total_Sales desc;

-- profit by category
select Category, sum(Profit) as Total_Profit
from sales_data
group by Category
order by Total_Profit desc;

-- sales by region
select Region, sum(Sales) as Total_Sales
from sales_data
group by Region
order by Total_Sales desc;

-- top 10 products by sales
select Product_Name, sum(Sales) as Total_Sales 
from sales_data
group by Product_Name
order by Total_Sales desc
limit 10;

-- top 10 customers by sales
select Customer_Name, sum(Sales) as Total_Sales
from sales_data
group by Customer_Name
order by Total_Sales desc
limit 10;

-- monthly sales trend
select YEAR(order_date) as Year, MONTH(order_date) as Month, sum(Sales) as Total_Sales
from sales_data
group by YEAR(order_date), MONTH(order_date)
order by Year, Month;

-- monthly profit trend
select YEAR(order_date) as Year, MONTH(order_date) as Month, sum(Profit) as Total_Profit
from sales_data 
group by YEAR(order_date), MONTH(order_date)
order by Year, Month;

-- top 10 states by sales
select state_province, sum(Sales) as Total_Sales
from sales_data
group by state_province
order by Total_Sales desc
limit 10;

-- top 10 cities by profit
select city, sum(Profit) as Total_Profit
from sales_data 
group by city
order by Total_Profit desc
limit 10;

-- average discount by category
select Category, avg(Discount) as Average_Discount
from sales_data
group by Category
order by Average_Discount desc;

-- most profitable products
select Product_Name, sum(Profit) as Total_Profit
from sales_data
group by Product_Name
order by Total_Profit desc
limit 10;

-- loss making products
select Product_Name, sum(Profit) as Total_Profit
from sales_data
group by Product_Name
having sum(Profit) < 0
order by Total_Profit;
