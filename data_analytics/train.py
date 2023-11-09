import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('data_analytics/train.csv')
'''
print(data.head(5))
print(data.tail(3))
print('number of rows:{},columns:{}'.format(data.shape[0],data.shape[1]))
print(data.info())
print(data.describe(include="all"))
print(data.columns)
print(data[['Name','Age']])
print(sum(data['Sex']=='male'))
data.rename(columns={'Sex':'Gender'},inplace=True)
print(data.columns)
print(data[data['Survived']==1]['Name'])
print(sum(data['Survived']==1))
print(data.isnull())
missing_value_percent = data.isnull().sum()*100/len(data)
print(missing_value_percent)
data.drop('Cabin',axis=1,inplace=True)
print(data.columns)
print(data['Embarked'])
data['Embarked'].fillna('S',inplace=True)
print(sum(data['Embarked'].isnull()))
print(data['Age'].head(15))
data['Age'].fillna('verilmeyib',inplace=True)
data.rename(columns={'Sex':'Gender'},inplace=True)
data['cinsiyet']=data['Gender'].map({'male':'kisi','female':'qadin'})
print(data.head(1))
'''







