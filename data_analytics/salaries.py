import pandas as pd
import numpy as np

data = pd.read_csv('data_analytics/Salaries.csv')

print(data.tail(10))
print(data.head(10))
print('number of rows is {},number of columns is {}'.format(data.shape[0],data.shape[1]))
print(data.info())
print(data.isnull())
print(data.columns)
data = data.drop(['Id','Notes','Agency','Status'],axis = 1)
print(data.columns)
print(data.describe())
print(data.describe(include='all'))
print(data.columns)
print(data['EmployeeName'].value_counts().head())
print(data['JobTitle'].nunique())

print(data[data['JobTitle'].str.contains('CAPTAIN')])
print(len(data[data['JobTitle'].str.contains('CAPTAIN')]))
print(data[data['JobTitle'].str.contains('CAPTAIN')].count())

print(data.columns)
print(data[data['JobTitle'].str.contains('fire',case=False)]['EmployeeName'])
print(data.columns)
print(data['BasePay'].describe())
print(data.columns)
data['EmployeeName']=data['EmployeeName'].replace('Not provided','Melumat yoxdu')
print(len(data[data['EmployeeName'].str.contains('Melumat yoxdu')]))
print(data[data.isnull().sum(axis=1)==5])
print(data.drop(data[data.isnull().sum(axis=1)==5].index,axis = 0))

print(data.isnull().sum(axis=1))
print(data[data['EmployeeName']=='Albert Pardini'] ['OtherPay'])
print(data[data['EmployeeName']=='Albert Pardini']['TotalPayBenefits'])
print(data[data['BasePay'].max()==data['BasePay']])
print(data.groupby('Year').mean()['BasePay'])


print(data.columns)
print(data.groupby('JobTitle').mean()['BasePay'])

print(data[data['JobTitle']=='Accountant']['BasePay'].mean())






