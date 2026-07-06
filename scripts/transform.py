import pandas as pd

# Cleans & transforms the extracted data. Returns a cleaned dataframe.
def transform_data(df):
    # create a copy to avoid modifying the original dataframe
    df = df.copy()
    
    # remove duplicate rows
    df = df.drop_duplicates()
    
    # remove rows with missing values
    df = df.dropna()
    
    # convert date columns to datetime format
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])
    
    # create new columns
    df["Order Year"]  = df["Order Date"].dt.year
    df["Order Month"]  = df["Order Date"].dt.month_name()
    df["Order Day"]  = df["Order Date"].dt.day
    
    # remove leading/trailimg spaces from text columns
    text_columns = [
        "Customer Name",
        "Category",
        "Sub-Category",
        "Product Name",
        "City",
        "State/Province",
        "Region",
        "Segment"
    ]
    
    for column in text_columns:
        df[column] = df[column].str.strip()
        
    # rename columns to snake_case
    df.columns = (
        df.columns
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
        .str.replace("/", "_")
    )
    
    return df

if __name__ == "__main__":
    df = pd.read_csv("data/raw/samplesuperstore.csv")
    
    transformed_df = transform_data(df)
    
    print(transformed_df.head())
    
    print("\nShape:", transformed_df.shape)
    
    print("\nColumns:")
    print(transformed_df.columns.tolist())