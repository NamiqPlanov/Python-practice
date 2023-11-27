import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import calendar
import datetime as dt

data = pd.read_csv('data_analytics/amazon.csv',encoding='iso-8859-1')
'''
print(data.head(5))
print(data.tail(5))
print(('{},{}').format(data.shape[0],data.shape[1]))

print(data.info())
print(data.isnull().sum())

print('is there any null value?{}'.format(data.isnull().values.any()))


print('is there any duplicated value?{}'.format(data.duplicated().values.any()))

data = data.drop_duplicates()
print('is there any duplicated value?{}'.format(data.duplicated().values.any()))

print(data.describe(include='all'))

sns.barplot(x='month_eng',y='number',data=monthly)
plt.show()

sns.barplot(x='year',y='number',data=yearly)
plt.xlabel('year')
plt.ylabel('number of fires')
plt.xticks(rotation=75)
plt.show()



plt.figure(figsize=(22,10))
sns.barplot(x='state',y='number',data = state)
plt.xlabel('states')
plt.ylabel('number of fires')
plt.xticks(rotation=85)
plt.show()

plt.figure(figsize=(20,10))
sns.barplot(x='year',y='number',data=fires_am_info)
plt.show()

'''
print(data['month'].unique())

data['month_eng']=data['month'].map({
    'Janeiro':'January',
    'Fevereiro':'February',
    'Março':'March',
    'Abril':'April',
    'Maio':'May',
    'Junho':'June',
    'Julho':'July',
    'Agosto':'August',
    'Setembro':'September',
    'Outubro':'October',
    'Novembro':'Nobvember',
    'Dezembro':'December'

})

print('number of registered fires-{}'.format(data.shape[0]))


monthly = data.groupby('month_eng')['number'].sum().reset_index()
yearly = data.groupby('year')['number'].sum().reset_index()
state = data.groupby('state')['number'].sum().reset_index()
fires_in_amazonas = data[data['state']=='Amazonas']['number'].sum()


fires_amazonas = data[data['state']=='Amazonas']

fires_am_info = fires_amazonas.groupby('year')['number'].sum().reset_index()

print(data[data['year']==2015].groupby('month_eng')['number'].sum().reset_index())









