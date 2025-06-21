import pandas as pd
s = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
#print(s)

data = {
    'name': ['Alice', 'Bob', None ,'Charlie'],
    'age': [25,None ,30, 35],
    'city': ['New York', 'Los Angeles', 'Chicago','Houston'],
    'salary': [700000, 80000, None, 90000],
    'gender':['female','male','male',None]
}
#df = pd.DataFrame(data)
#print(df)

#reading a csv, json,excel file with pandas dataframe
#df_csv = pd.read_csv('data.csv')
#df_json = pd.read_json('data.json')
#df_excel = pd.read_excel('data.xlsx')

#print(df["name"])
#print(df.loc[0])
#summary commands
#df.describe() #summary of the dataframe
#df.info()
#print(df['city'].value_counts())

#random code stuff to check how it works
df = pd.DataFrame(data)
print('Orignial DataFrame:\n',df)

#after filtering out the null values
df = df.dropna()
print('DataFrame after dropping null values:\n',df)

df["name"] = df['name'].str.strip().str.title()
df['gender'] = df['gender'].str.strip().str.capitalize()
print('DataFrame after cleaning name \n',df)

df["high_salary"] = df['salary'] > 100000
print('DataFrame with high salary column:\n',df)
