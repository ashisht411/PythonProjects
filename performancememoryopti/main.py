import pandas as pd
start = time.time()
chunk_iter = pd.read_csv("large_sales_data.csv", chunksize=100000)

total_rows = 0
for chunk in chunk_iter:
    total_rows += len(chunk)
    # Apply logic per chunk if needed
    print(f"Processed {total_rows} rows so far.")

df = pd.read_csv("large_sales_data.csv")

before = df.memory_usage(deep=True).sum()

# Convert float64 → float32 and int64 → int32
df["Sales"] = pd.to_numeric(df["Sales"], downcast="float")
df["Quantity"] = pd.to_numeric(df["Quantity"], downcast="integer")

after = df.memory_usage(deep=True).sum()
print(f"Before: {before / 1_000_000:.2f} MB")
print(f"After: {after / 1_000_000:.2f} MB")

df["Region"] = df["Region"].astype("category")
df["Product"] = df["Product"].astype("category")
import time


df = pd.read_csv("large_sales_data.csv")
# (some transformation here)

print(f"Time taken: {time.time() - start:.2f} seconds")


