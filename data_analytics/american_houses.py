import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv('data_analytics/American_houses.csv')

'''

print(data.dtypes)
print(data.describe(include='all'))


numeric_cols = ['Zip Code','Price','Beds','Baths','Living Space','Zip Code Population','Median Household Income']
data[numeric_cols].hist(edgecolor='green')
plt.show()


arr = ['Beds','Baths','Living Space','Price']
data[arr].hist(bins = int(input('enter the bin please:')),edgecolor=input('enter the color of the edge please:'))
plt.show()


plt.scatter(data['Living Space'],data['Price'],alpha = 0.7)
plt.show()



numeric_cols2 = data.select_dtypes(include='number')
numeric_correl = numeric_cols2.corr()
sns.heatmap(numeric_correl,annot=True)
plt.show()



grouped_data = data.groupby('City')
summary_info = data.agg({
    'Median Household Income':'median',
    'Price':'mean'
}).reset_index()
print(summary_info)


sns.scatterplot(x='Median Household Income',y='Price',data=data)
plt.xlabel('household income')
plt.ylabel('Prices')
plt.xticks(rotation=84)
plt.show()

data['new feature'] = data['Price']/data['Living Space']
print(data.columns)
'''
data=data.dropna()




