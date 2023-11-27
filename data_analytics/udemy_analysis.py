import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('data_analytics/udemy_courses.csv',parse_dates=['published_timestamp'])
'''
print(data.head(10))
print(data.tail(5))
print(data.shape)
print('number of rows:{}'.format(data.shape[0]))
print('number of cols:{}'.format(data.shape[1]))
print(data.info())

print(data.isnull().values.any())

print(data[data.duplicated()]['course_title'])
data = data.drop_duplicates()
print(data.duplicated().values.any())'

colors = ['yellow','green','violet','grey']
sns.countplot(data['subject'],palette=colors)
plt.ylabel('subjects')
plt.yticks(rotation=55)
plt.show()

print(data.columns)
print(data['level'].unique())

print(data['is_paid'].value_counts())
a1=data.groupby(['is_paid']).mean()
print(a1)

sns.barplot(x='is_paid',y='num_subscribers',data=data)
plt.show()


colors = ['grey','pink','green','violet']
plt.figure(figsize=(11,6))
sns.barplot(x='level',y='num_subscribers',data=data,palette=colors)
plt.xlabel('Levels')
plt.ylabel('Number of subscribers')
plt.xticks(rotation=65)
plt.show()

print(data[data['num_lectures'].max()==data['num_lectures']]['subject'])

print(data.sort_values(by='num_subscribers')['course_title'].head(10))


print(data.columns)
plt.figure(figsize=(13,6))
sns.scatterplot(x='price',y='num_reviews',data=data)
plt.show()


print(data['course_title'].str.contains('Python'))

print(data[data['course_title'].str.contains('Python')].sort_values(by='num_subscribers',ascending=False).head(10))



print(data.head(1))
sns.countplot(x='year',data=data)
plt.show()
'''
data['year'] = data['published_timestamp'].dt.year
print(data.columns)
print(data.groupby('year')['subject'].value_counts())















