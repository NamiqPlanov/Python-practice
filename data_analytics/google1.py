import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('data_analytics/google1.csv')
'''
print(data.head(5))
print(data.tail(3))
print('number of rows is {}'.format(data.shape[0]))
print('number of columns is {}'.format(data.shape[1]))
print(data.info())
print(data.describe())
print(data.columns)
print(data[data['App'].str.contains('Astrology')])

print(data['Rating'].describe())
print(data['Rating'].mean())
print(data['Category'].unique())
print(data['Category'].nunique())
print(data.groupby('Category')['Rating'].mean().sort_values(ascending=False))
print(data.columns)
print(data[data['Rating']==5])
print(sum(data['Rating']==5))
print(sum(data['Type']=='Free'))
print(sum(data['Type']=='Paid'))
print(data['Type'].value_counts())
print(data['Reviews'].max())
print(data[data['Reviews'].max()==data['Reviews']])
'''
print(data.columns)
index = data['Reviews'].sort_values(ascending=False).head(5).index
print(data.iloc[index]['App'])


