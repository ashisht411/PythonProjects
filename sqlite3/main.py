import pandas as pd

# Load the cleaned CSV
df = pd.read_csv("filename.csv")

# Optional: Reduce size
df["Sales"] = pd.to_numeric(df["Sales"], downcast="float")
df["Quantity"] = pd.to_numeric(df["Quantity"], downcast="integer")

import sqlite3

# Connect to SQLite DB (will create the file if it doesn't exist)
conn = sqlite3.connect("sales_data.db")

# Write DataFrame to SQLite table
df.to_sql("sales", conn, if_exists="replace", index=False)

with sqlite3.connect("sales_data.db") as conn:
    result = pd.read_sql_query("""
        SELECT Region, SUM(Sales) AS Total_Revenue
        FROM sales
        GROUP BY Region
        ORDER BY Total_Revenue DESC
    """, conn)

print(result)

