import pandas as pd
import numpy as np
import requests #for making api calls
import matplotlib.pyplot as plt
import seaborn as sns

#fetching the data from the api
response = requests.get('https://disease.sh/v3/covid-19/countries')
data = response.json()
df = pd.DataFrame(data)
print(df[['country', 'cases', 'deaths', 'recovered']].head(10))

#cleaning the data
df.dropna(subset=['country','cases'],inplace=True)
df.rename(columns={'country': 'Country', 'cases': 'Cases', 'deaths': 'Deaths', 'recovered': 'Recovered'}, inplace=True)

#Aggregate the data(optional)
summary = df.groupby('Country')[['Cases','Deaths']].sum().reset_index()
#sorted by top 10 countries with most cases
top10 = summary.sort_values(by='Cases', ascending=False).head(10)
print("\nTop 10 countries with most cases:\n",top10)

#plotting the data using matplotlib and seaborn
plt.figure(figsize=(12, 6))
sns.barplot(data=top10,x="Country",y="Cases",palette="twilight",hue="Country")
plt.title('Top 10 Countries with Most COVID-19 Cases')
plt.xlabel('Country')
plt.ylabel('Total Cases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#outputting it as a csv file
summary.to_csv('covid_summary.csv', index=False)