import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data_analytics/IMDB-Movie-Data.csv')



print(data.head(10))
print(data.tail(10))

print('number of rows:{}'.format(data.shape[0]))
print('number of columns:{}'.format(data.shape[1]))

print(data.info())
is_dup_value = data.duplicated().any()
print('Is there any duplicated value? {}'.format(is_dup_value))
print(data.describe())
print(data.sort_values(by='Runtime (Minutes)',ascending=False).head(5)['Runtime (Minutes)'])
print(data[data['Runtime (Minutes)']>180]['Title'])

data_minutes = data[data['Runtime (Minutes)']>160]
print(data_minutes.head(5)['Title'])

print(data.groupby('Year')['Votes'].mean())
print(data.groupby('Year')['Revenue (Millions)'].mean())

sns.barplot(x='Year',y='Revenue (Millions)',data=data)
plt.show()
print(data.groupby('Director')['Rating'].mean())

data = data.dropna(axis = 0,inplace=True)
print(type(data))
