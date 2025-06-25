import pandas as pd

df = pd.DataFrame({
    "Region": ["East", "West", "East", "North"],
    "Date": ["2023-01-01", "2023-01-08", "2023-02-15", "2023-02-22"],
    "Sales": [1000, 1500, 1200, 1100]
})

df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.to_period("M").astype(str)
monthly_sales = df.groupby(["Region", "Month"])["Sales"].sum().reset_index()

df["Week"] = df["Date"].dt.to_period("W").astype(str)
weekly_sales = df.groupby(["Region", "Week"])["Sales"].sum().reset_index()

df["Days_Since_First"] = (df["Date"] - df["Date"].min()).dt.days
print(df[["Region", "Date", "Sales","Days_Since_First"]])
df.set_index("Date", inplace=True)

# Total sales by week (across all regions)
weekly = df["Sales"].resample("W").sum()


