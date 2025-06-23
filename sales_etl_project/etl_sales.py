import os
import glob
import argparse
import logging
import pandas as pd
import sqlite3

#Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

#Extract step
def extract_data(input_folder):
    logging.info("Extracting data from CSV files...")
    all_files = glob.glob(os.path.join(input_folder, "*.csv"))
    if not all_files:
        logging.error(f"No CSV files found in {input_folder}.")
        raise FileNotFoundError(f"No CSV files found in {input_folder}.")
    dfs = [pd.read_csv(file) for file in all_files]
    combined_df = pd.concat(dfs, ignore_index=True)
    return combined_df

# Transform step
def transform_data(df):
    logging.info("Transforming data...")

    # Example cleaning: drop rows with null sales
    df.dropna(subset=["Region", "Date", "Sales"], inplace=True)

    # Convert 'Sales' to numeric (in case of bad data)
    df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
    df.dropna(subset=["Sales"], inplace=True)

    # Convert 'Date' to datetime
    df["Date"] = pd.to_datetime(df["Date"])

    # Extract month
    df["Month"] = df["Date"].dt.to_period("M").astype(str)

    # Group by Region and Month, then sum Sales
    grouped = df.groupby(["Region", "Month"])["Sales"].sum().reset_index()

    return grouped

#Load step
def load_data(df, output_csv, output_db):
    logging.info("Loading data to CSV and SQLite...")

    # Save to CSV
    df.to_csv(output_csv, index=False)

    # Ensure output directory for DB exists
    db_dir = os.path.dirname(output_db)
    if db_dir:
        os.makedirs(db_dir, exist_ok=True)

    # Save to SQLite
    conn = sqlite3.connect(output_db)
    df.to_sql("monthly_sales", conn, if_exists="replace", index=False)
    conn.close()

#Main function
def main(input_folder, output_csv, output_db):
    try:
        raw_df = extract_data(input_folder)
        transformed_df = transform_data(raw_df)
        load_data(transformed_df, output_csv, output_db)
        logging.info("ETL Job Completed Successfully!")
    except Exception as e:
        logging.error(f"ETL Job failed: {e}")
        raise

#argparse setup
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sales ETL Job")
    parser.add_argument("--input", required=True, help="Path to folder containing raw CSVs")
    parser.add_argument("--output_csv", default="output/sales_summary.csv", help="Path to output CSV")
    parser.add_argument("--output_db", default="output/sales.db", help="Path to output SQLite DB")
    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.output_csv), exist_ok=True)
    main(args.input, args.output_csv, args.output_db)