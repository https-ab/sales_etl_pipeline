import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

def load_data(df, output_path):
    df.to_csv(output_path, index=False)
    print("Data loaded successfully!")
    print(f"File saved at: {output_path}")
    

def load_to_mysql(df):
    username = "root"
    # password = "anushka@2002"
    password = quote_plus("anushka@2002")
    host = "localhost"
    port = "3306"
    database = "sales_db"
    
    engine = create_engine(
        f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
    )
    
    df.to_sql(
        name="sales_data",
        con=engine,
        if_exists="replace",
        index=False
    )

    print("Data loaded into MySQL successfully!")
    
    
if __name__ == "__main__":
    from extract import extract_data
    from transform import transform_data

    input_file = "data/raw/samplesuperstore.csv"
    output_file = "data/processed/cleaned_superstore.csv"

    # Extract
    df = extract_data(input_file)

    # Transform
    transformed_df = transform_data(df)

    # Save cleaned CSV
    load_data(transformed_df, output_file)

    # Load into MySQL
    load_to_mysql(transformed_df)