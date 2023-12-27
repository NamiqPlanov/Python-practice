import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('data_analytics/Video_Games_Sales.csv')

'''
print(data.dtypes)

print('is there any null value?{}'.format(data.isnull().values.any()))
print('is there any null value after dropping?{}'.format(data.isnull().values.any()))
print(data.duplicated().sum())

print(numeric.describe())

for i in metric:
    print('Unique values of {}:'.format(i))
    print(data[i].unique())
    
data['Year'].hist()
plt.show()

info1.plot(kind='bar',color='grey')
plt.title('Top 5 platforms by the number of games')
plt.xlabel('Platforms')
plt.ylabel('Number of games')
plt.show()


plt.figure(figsize=(8,6))
info2.plot(kind='bar',color='green')
plt.title('Distribution of game genres')
plt.xlabel('Game genres')
plt.tight_layout()
plt.show()

plt.pie(info2,labels=info2.index,colors = plt.cm.tab20.colors)
plt.show()

plt.scatter(data['Year'],data['Global'],alpha=0.9)
plt.title('Scatterplot between Year and Global')
plt.show()

game_title.plot(kind='bar')
plt.title('Top Game Titles for global')
plt.xlabel('Games')
plt.tight_layout()
plt.show()

publishers.plot(kind='bar',color='green')
plt.title('Top publishers of games')
plt.xlabel('Publishers')
plt.tight_layout()
plt.show()

sns.barplot(x='Genre',y='Review',data=info5)
plt.show()
print(data[['Total Sales','North America','Europe','Japan','Rest of World']])

print('The platform with highest global sales is {}'.format(max1))

info7.plot(kind='line',marker='o',color='green',linestyle='-')
plt.title('Sales trends over years')
plt.xlabel('Years')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

print('The correlation between Review and Global - {}'.format(corr1))

for area in areas:
    corr2 = data['Global'].corr(data[area])
    print('The correleation for Global with {} is {}'.format(area,corr2))

print('The platform with the highest average Review Score is {}'.format(max2))
'''


data = data.dropna()
numeric =data.select_dtypes(include='number')
metric = ['Game Title','Platform','Genre','Publisher']
info1 = data['Platform'].value_counts().head(5)
info2 = data['Genre'].value_counts().head(5)
info3 = data.sort_values(by='Global').head(5)['Game Title'].values[0:5]
game_title = data[data['Game Title'].isin(info3)]['Game Title'].value_counts()
info4 = data.sort_values(by='Game Title').head(5)['Publisher'].values[0:5]
publishers = data[data['Publisher'].isin(info4)]['Publisher'].value_counts()
info5 = data.sort_values(by='Review').head(1)
data['Total Sales'] = data['North America']+data['Europe']+data['Japan']+data['Rest of World']
info6 = data.groupby('Platform')['Global'].sum()
max1 = info6.idxmax()
info7 = data.groupby('Year')['Europe'].sum()
corr1 = data['Review'].corr(data['Global'])

areas = ['North America', 'Europe', 'Japan', 'Rest of World']
info8 = data.groupby('Platform')['Review'].mean()
max2 = info8.idxmax()






