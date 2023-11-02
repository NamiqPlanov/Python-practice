import pandas as pd

data = pd.read_csv('data_analytics/dataset1')
'''print('number of rows is {},number of columns is {}'.format(data.shape[0],data.shape[1]))
print(data.head(6))
print(data.tail(6))
print(data.dtypes)
print(data.isnull())
print(len(data.columns))
print(data.info())
print(data['Purchase Price'].max())
print(data[(data['Purchase Price']>15) & (data['Purchase Price']<=45)])
print(data['Purchase Price'].mean())
def int1(x):
    return x//2

data['Purchase Price half'] = data['Purchase Price'].apply(int1)
print(data.columns)
print(len(data[data['Language']=='fr']))
print(data[data['Language']=='fr'].count())
print(data[data['Job'].str.contains('engineer')])
print(len(data[data['Job'].str.contains('engineer')]))
print(data[data['IP Address']=="132.207.160.22"]['Email'])
print(data[(data['CC Provider']=='Mastercard')&(data['Purchase Price']>50)])
print(len(data[(data['CC Provider']=='Mastercard') & (data['Purchase Price']>50)]))
print(data[data['Credit Card']==4664825258997302] ['Address'])
print(len(data[data['AM or PM']=='AM']))
print(len(data[data['AM or PM']=='PM']))
print(data['AM or PM'].value_counts())
print(data.columns)
def expiration_date():
    count = 0
    for i in data['CC Exp Date']:
        if i.split('/')[1]=='20':
            count+=1
    return count
print(expiration_date())
print(len(data[data['CC Exp Date'].apply(lambda x:x[3:]=='20')]))
'''




