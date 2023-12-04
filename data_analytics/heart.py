import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data_analytics/heart.csv')

'''

print(data['target'].value_counts())

sns.countplot(data['target'])
plt.legend(labels=([0,1],['yes','no']))
plt.show()

sns.distplot(data['age'],bins=15)
plt.show()

print(data['sex'].value_counts())

sns.countplot(x='sex',hue='target',data=data)
plt.xticks([1,0],['Male','Female'])
plt.legend(labels=['Disease','No-disease'])
plt.show()

plt.figure(figsize=(17,7))
sns.heatmap(data.corr(),annot=True)
plt.show()


color = ['green','yellow','blue','grey']
sns.countplot(data['chest_pain_type'],palette=color)
plt.show()


sns.barplot(x='chest_pain_type',y='target',data=data)
plt.show()




sns.countplot(x='fbs',hue='target',data=data)
plt.legend(labels=['Disease','No-disease'])
plt.show()


sns.distplot(data['trestbps'],bins=18)
plt.show()


data['trestbps'].hist()
plt.show()
'''


data['chest_pain_type'] = data['cp'].map({
    0:'typical angina',
    1:'atypical angina',
    2:'non-anginal pain',
    3:'asymptomatic'


})










