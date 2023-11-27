import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


data = pd.read_csv('data_analytics/youtube_channels.csv')


'''
print(data.head(-5))
print(data.tail(-5))

print(data.shape)
print('number of rows:{}'.format(data.shape[0]))
print('number of columns:{}'.format(data.shape[1]))
print(data.info())
print(data.describe())

data = data.replace('--',np.nan,regex=True)
print(data.head(26))

print(data.isnull().sum())
print(data.columns)

print(data.dtypes)


print(data.head(10))
print(data.dtypes)


print(data.dtypes)


data['Rank']=data['Rank'].str[0:-2]
data['Rank']=data['Rank'].str.replace(',','').astype('int')


data['Grade'] = data['Grade'].map({'A++':5,'A+':4,'\xa0':0,'A':3,'A-':2,'B+':1})
data['Grade'] = data['Grade'].astype('int')
print(data['Subscribers'])



print(data.columns)
sns.barplot(x='Grade',y='Average views',data=data)


print(data.sort_values(by='Video Uploads',ascending=False).head(5))
sns.barplot(x='Grade',y='Subscribers',data=data)
print(data.dtypes)
'''

data = data.replace('--',0,regex=True)
data['Subscribers'] = data['Subscribers'].astype('int')
data['Video Uploads'] = data['Video Uploads'].astype('int')
print(data.columns)
data['Average views']=data['Video views']/data['Video Uploads']



sns.barplot(x='Grade',y='Video views',data=data)
plt.show()








