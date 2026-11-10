import pandas as pd
import os

def clean_and_process_excel(input_file, output_file):
    """
    Automates Excel data cleaning, removes duplicates, handles missing values,
    and exports a formatted clean dataset.
    """
    print(f"[INFO] Loading data from: {input_file}")
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print("[ERROR] Input file not found! Please check the file path.")
        return

    # Load Excel file into pandas DataFrame
    df = pd.read_excel(input_file)

    print("[INFO] Processing data...")

    # 1. Strip whitespace from text columns
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype(str).str.strip()

    # 2. Remove duplicate rows based on all columns
    initial_count = len(df)
    df.drop_duplicates(inplace=True)
    removed_duplicates = initial_count - len(df)
    print(f"[INFO] Removed {removed_duplicates} duplicate records.")

    # 3. Fill missing values (NaN) with default placeholders
    df.fillna({"Status": "Pending", "Notes": "N/A"}, inplace=True)

    # 4. Standardize column names (lowercase with underscores)
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

    # Save the cleaned output to a new Excel file
    df.to_excel(output_file, index=False)
    print(f"[SUCCESS] Cleaned data exported successfully to: {output_file}")

if __name__ == "__main__":
    # Example usage:
    # Change 'raw_data.xlsx' to your input file path
    input_path = "raw_data.xlsx"
    output_path = "cleaned_data.xlsx"

    # Run the automation pipeline
    clean_and_process_excel(input_path, output_path)