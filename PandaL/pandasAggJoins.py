import pandas as pd

data = {
    "Department": ["Sales", "Sales", "HR", "HR", "IT"],
    "Employee": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Salary": [50000, 60000, 45000, 47000, 70000]
}
df = pd.DataFrame(data)

print(df.groupby('Department')['Salary'].mean())
print(df.groupby('Department')['Salary'].agg(['mean', 'max', 'min']))

df1 = pd.DataFrame({
  'empid': [1, 2, 3],
  'name': ['Alice', 'Bob', 'Charlie']})

df2 = pd.DataFrame({
  'empid': [1, 2, 4],
  'department': ['Sales', 'HR', 'IT']})

merge_df = pd.merge(df1,df2,on ='empid',how='inner')
print(merge_df)

grouped = df.groupby('Department')['Salary'].mean().reset_index()
sorted_group = grouped.sort_values(by='Salary', ascending=True)
print(sorted_group[sorted_group['Salary'] > 50000])