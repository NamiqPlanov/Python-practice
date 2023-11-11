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
print(data['Embarked'].unique())
print(data['Embarked'].nunique())
print(pd.get_dummies(data,columns=['Sex']))
print(pd.get_dummies(data,columns=['Sex']))
data1 = pd.get_dummies(data,columns=['Sex'],drop_first=True)
print(data1.head(1))
print(data.columns)
print('Number of survived people-{}'.format(sum(data['Survived']==1)))
print('Number of died people-{}'.format(sum(data['Survived']==0)))
sns.countplot(data['Survived'])#-see table of survived and dies people
print('Number of people,that were in the first class-{}'.format(sum(data['Pclass']==1)))
print('Their names: \n {}'.format(data[data['Pclass']==1]['Name']))

print('Number of people,that were in the second class-{}'.format(sum(data['Pclass']==2)))
print('Their names: \n {}'.format(data[data['Pclass']==2]['Name']))

print('Number of people,that were in the third class-{}'.format(sum(data['Pclass']==3)))
print('Their names: \n {}'.format(data[data['Pclass']==3]['Name']))
print(data['Pclass'].value_counts())
plt.figure(figsize=(3,3))
data['Pclass'].hist()
colors = ['green','blue','red']
sns.barplot(x='Pclass',y='Survived',data=data,palette=colors)

plt.show()
plt.show()
sns.barplot(x='Sex',y='Survived',data=data) 
colors1 = ['violet','yellow']
sns.barplot(x='Sex',y='Survived',data=data,palette=colors1)
plt.show()print(data.columns)
print(data['SibSp'])
print(data['Parch'])
'''

data['1 or 0'] = data['SibSp']+data['Parch']
print(data.head(5))












