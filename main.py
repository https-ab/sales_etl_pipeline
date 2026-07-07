from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data, load_to_mysql

# File paths
input_file = "data/raw/samplesuperstore.csv"
output_file = "data/processed/cleaned_superstore.csv"

print("Starting ETL Pipeline...")

# Extract
df = extract_data(input_file)

# Transform
transformed_df = transform_data(df)

# Save cleaned CSV
load_data(transformed_df, output_file)

# Load into MySQL
load_to_mysql(transformed_df)

print("ETL Pipeline completed successfully!")