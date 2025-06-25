import pandas as pd
import numpy as np

# Target ~100MB file by generating ~2.5 million rows
num_rows = 2_000_000
regions = ['North', 'South', 'East', 'West']
products = ['Widget', 'Gadget', 'Thingamajig', 'Doohickey']

df = pd.DataFrame({
    "Date": pd.date_range(start="2022-01-01", periods=num_rows, freq='min'),
    "Region": np.random.choice(regions, size=num_rows),
    "Product": np.random.choice(products, size=num_rows),
    "Quantity": np.random.randint(1, 20, size=num_rows),
    "Sales": np.round(np.random.uniform(10.0, 500.0, size=num_rows), 2)
})

df.to_csv("performancememoryopti/filename.csv", index=False)
