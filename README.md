# Sales ETL Pipeline

## Project Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline built using Python, Pandas, and MySQL.

The pipeline:
- Extracts sales data from a CSV file
- Cleans and transforms the data using Pandas
- Saves the cleaned dataset as a new CSV
- Loads the cleaned data into a MySQL database
- Performs SQL-based business analysis
- Automates the complete workflow using a single Python script

---

## Technologies Used

- Python
- Pandas
- NumPy
- MySQL
- SQLAlchemy
- PyMySQL
- Matplotlib
- Seaborn
- Jupyter Notebook
- VS Code

---

## Project Structure

```text
sales_etl_pipeline/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── test_connection.py
│
├── sql/
│   └── queries.sql
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Features

- Data Extraction from CSV
- Data Cleaning and Transformation
- Save Processed Data
- Load Data into MySQL
- SQL Business Analysis
- Automated ETL Pipeline

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/https-ab/sales_etl_pipeline.git
cd sales_etl_pipeline
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the ETL pipeline

```bash
python main.py
```

---

## SQL Analysis

The project includes SQL queries for:

- Total Sales
- Total Profit
- Average Sales
- Sales by Category
- Sales by Region
- Top Customers
- Top Products
- Monthly Sales Trend
- Monthly Profit Trend
- Average Discount by Category
- Loss-Making Products

---

## Author

**Anushka Bhasme**