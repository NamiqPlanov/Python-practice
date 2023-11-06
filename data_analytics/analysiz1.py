import pandas as pd
dict1 = {'Name':['Namiq','Ayxan','Ilkin','Eli','Eltun','Esed','Zaur'],
'Place of birth':['Baku','Baku','Baku','Ganja','Shamkir','Baku','Daghistan'],
'Age':[19,16,21,20,21,20,19],
'Points':[93,94,91,92,85,86,93]}
data = pd.DataFrame(dict1)
print(data.head(3))
print(data.tail(3))
print('the number of rows and columns are {}'.format(data.shape))
print('Number of rows is {}'.format(data.shape[0]))
print('Number of columns is {}'.format(data.shape[1]))
print('Data info: {}'.format(data.info()))
print(data.isnull().sum(axis=1))
print(data.isnull().sum())
print(data.isnull())
print(data.describe())
print(data.describe(include='all'))
print(data)
print(data['Name'])
print(data['Name'].unique())
print(data['Name'].nunique())
print(data['Age'].value_counts())
print(data['Points']>91)
print(data[data['Points']>=92])
print((data['Age']>15) & (data['Age']<20))
print(data[(data['Age']>15) & (data['Age']<20)])
print(len(data[(data['Age']>15) & data['Age']<=19]))
print(sum(data['Age'].between(16,19)))
print(data['Age'].mean())
print(data['Points'].mean())
print(data['Age'].min())
print(data['Age'].max())
def divide(a):
    return a//2

data['Half Points']=data['Points'].apply(divide)
print(data)
print(data['Age'].apply(lambda x:x//2))
print(data['Name'].apply(len))
data['Baku or other city'] = data['Place of birth'].map({'Baku':1})
print(data['Baku or other city'])
print(data['Age']>19)
print(data.drop(['Age'],axis=1))
print(data.columns)

print(data.sort_values(by = 'Points'))
print(data.sort_values(by='Age'))







