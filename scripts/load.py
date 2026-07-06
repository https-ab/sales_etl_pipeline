import pandas as pd

def load_data(df, output_path):
    df.to_csv(output_path, index=False)
    print("Data loaded successfully!")
    print(f"File saved at: {output_path}")
    

if __name__ == "__main__":
        from extract import extract_data
        from transform import transform_data
        
        input_file = "data/raw/samplesuperstore.csv"
        output_file = "data/processed/cleaned_superstore.csv"
        
        # extract
        df = extract_data(input_file)
        
        # transform
        transformed_df = transform_data(df)
        
        # load
        load_data(transformed_df, output_file)