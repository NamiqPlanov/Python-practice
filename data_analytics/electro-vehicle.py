import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd

data=  pd.read_csv('data_analytics/electro-vehicle.csv')


'''

electric_range = data['Electric Range'].describe()
base = data['Base MSRP'].describe()
print(electric_range)
print(base)
print('Median of the electric range - {}'.format(data['Electric Range'].median()))
print('Mean of the electric range - {}'.format(data['Electric Range'].mean()))
print('Standart deviation of the electric range - {}'.format(data['Electric Range'].std()))
print('Median of the base msrp - {}'.format(data['Base MSRP'].median()))
print('Mean of the base msrp - {}'.format(data['Base MSRP'].mean()))
print('Standart Deviation of the base msrp - {}'.format(data['Base MSRP'].std()))

print(data['Make'].value_counts())
print('-------------------------------')
print(data['Electric Vehicle Type'].value_counts())


arr = ['Electric Range','Base MSRP']
numbered_arr = data[arr].apply(pd.to_numeric,errors = 'coerce')
sns.heatmap(numbered_arr.corr(),annot=True)
plt.show()

sns.countplot(x='Clean Alternative Fuel Vehicle (CAFV) Eligibility',data=data)
plt.show()


print(data.columns)
print(data['Electric Vehicle Type'].unique())
info1 = data[data['Electric Vehicle Type']=='Battery Electric Vehicle (BEV)'].groupby('City').size().reset_index(name = 'Number of electric vehicles')
top_cities = info1.sort_values(by='Number of electric vehicles',ascending=False).head(6)
sns.barplot(x='City',y='Number of electric vehicles',data=top_cities)
plt.xlabel('Cities')
plt.ylabel('Number of electric cars')
plt.xticks(rotation=80)
plt.show()


info2 = data.groupby('Model').size().reset_index(name='Number of vehicles')
top_models = info2.sort_values(by='Number of vehicles',ascending=False).head(5)
sns.barplot(x='Model',y='Number of vehicles',data = top_models,color='green')
plt.xlabel('Top 5 car models')
plt.show()
'''

data = data.dropna()

data['Postal Code']=data['Postal Code'].astype('int')
data['2020 Census Tract'] = data['2020 Census Tract'].astype('int')


print(data.columns)


info3 = data.groupby('Legislative District').size().reset_index(name='Number of vehicles')
districts = info3.sort_values(by='Number of vehicles',ascending=False).head(6)
sns.barplot(x='Legislative District',y='Number of vehicles',data=districts)
plt.show()








