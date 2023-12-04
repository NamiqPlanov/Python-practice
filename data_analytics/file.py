import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt 


data = pd.read_csv('data_analytics/sales.csv',encoding='unicode-escape')

'''
print(data.shape)
print(data.columns)


data['Amount']=data['Amount'].replace(0,133)

data.drop(['Status','unnamed1'],axis=1,inplace=True)
data.dropna(inplace=True)
print(data.isnull().sum())


plt.figure(figsize=(13,7))
sns.countplot(x='Gender',data=data)
plt.xticks(rotation=55)
plt.xticks(['F','M'],['Female','Male'])
plt.xlabel('Gender')
plt.show()


print(data.columns)
print(data['Marital_Status'].unique())
sns.countplot(x='Gender',hue='Marital_Status',data=data)
plt.xticks(['F','M'],['Female','Male'])
plt.legend(['0','1'])
plt.show()

stattistics = sns.countplot(x = 'Gender',hue='Age Group',data=data)
for info in stattistics.containers:
    stattistics.bar_label(info)
    plt.show()
    
ax=sns.countplot(x='Gender',data=data)
for bars in ax.containers:
    ax.bar_label(bars)
    plt.show()
    
    
gender_sales = data.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
color = ['blue','green']
sns.barplot(x='Gender',y='Amount',data=gender_sales,palette=color)
plt.show()

age_group_info = sns.countplot(x='Age Group',hue='Gender',data=data)
for info in age_group_info.containers:
    age_group_info.bar_label(info)
plt.show()


amount_age_group = data.groupby('Age Group',as_index=False)['Amount'].sum().sort_values('Amount',ascending=False)
print(amount_age_group)
sns.barplot(x='Age Group',y='Amount',data=amount_age_group)
plt.show()


print(data.columns)
state_orders = data.groupby('State',as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(5)
plt.figure(figsize=(12,6))
sns.barplot(x='State',y='Orders',data=state_orders)
plt.show()


sales_states = data.groupby('State',as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(6)
print(sales_states)

sns.barplot(x='State',y='Amount',data=sales_states)
plt.show()

status = sns.countplot(data=data,x='Marital_Status')
for info in status.containers:
    status.bar_label(info)
plt.show()


status_gender = data.groupby(['Marital_Status','Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x='Marital_Status',y='Amount',hue='Gender',data=status_gender)
plt.show()


occupation = sns.countplot(data=data,x='Occupation')
for info in occupation.containers:
    occupation.bar_label(info)
plt.show()


sales_occupation = data.groupby('Occupation',as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(5)
print(sales_occupation)
sns.barplot(x='Occupation',y='Amount',data=sales_occupation)
plt.show()

print(data.columns)

products = sns.countplot(x='Product_Category',data=data)
for info in products.containers:
    products.bar_label(info)

plt.show()

products_sales = data.groupby('Product_Category',as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
plt.figure(figsize=(20,7))
sns.barplot(x='Product_Category',y='Amount',data=products_sales)
plt.show()


product_id = data.groupby('Product_ID',as_index=False)['Orders'].sum().sort_values('Orders',ascending=False)
sns.barplot(x='Product_ID',y='Orders',data=product_id)
plt.show()
'''
















