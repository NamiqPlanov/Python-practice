import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data_analytics/adult.csv')
'''
print(data.head(5)['workclass'])
print(data['workclass'].replace('?','not given'))
print(data.head(10))
print(data.tail(10))
print('number of rows-{}, numbers of columns-{}'.format(data.shape[0],data.shape[1]))
print(data.info())
print(data.sample(frac=0.6))
print(data.sample(frac=0.3,random_state=110))
print(data.isnull().sum())
print(sns.heatmap(data.isnull()))
print(data.isin(['?']).sum())
data['workclass']=data['workclass'].replace('?',np.nan)
print(data['workclass'].head(6))
data['occupation']= data['occupation'].replace('?',np.nan)
data['native-country'] = data['native-country'].replace('?',np.nan)
print(data[data['occupation']=='?'])
print(data.isin(['?']).sum())
print(sns.heatmap(data.isnull()))
missingdata_percent = data.isnull().sum()* 100/len(data)
print(missingdata_percent)
print(data.shape)
data.dropna(how = "any",inplace = True)
print(data.shape)
dup = data.duplicated().any()
print('duplicated values:{}'.format(dup))
dup_drop = data.drop_duplicates()
print(dup_drop)
print(data.describe())
print(data.describe(include='all'))
print(data['education'].unique())
print(data['education-num'].unique())
print(data.columns)
data= data.drop(['educational-num','capital-gain','capital-loss'],axis=1)
print(data.columns)
print(data['age'].describe())
print(data['age'].hist())
print(sum((data['age']>=17)&(data['age']<=48)))
print(sum(data['age'].between(17,48)))
print(data['workclass'].describe())
plt.figure(figsize=(7,7))
data['workclass'].hist()
plt.show()

print(data.columns)
print('number of bachelor degrees:{}'.format(sum(data['education']=='Bachelors')))
print('number of masters degrees:{}'.format(sum(data['education']=='Masters')))

print(sum(data['education'].isin(['Bachelors','Masters'])))
print(data.columns)
sns.boxplot(x='age',y='salary',data=data)
'''
def salary_update(a):
    if a =='<=50k':
        return 0
    if a=='>50k':
        return 1

data['encoded'] =data['income'].apply(salary_update)
print(data['encoded'].head())













