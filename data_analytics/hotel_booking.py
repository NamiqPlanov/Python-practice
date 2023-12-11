import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data_analytics/hotel_bookings.csv')



print(data.head(5))
print(data.describe)

print(data.isnull().sum())




color = ['green','blue']
info_hotels = sns.countplot(x='hotel',data=data,palette=color)
for info1 in info_hotels.containers:
    info_hotels.bar_label(info1)
plt.xlabel('Hotels')
plt.ylabel('Number of hotels')
plt.xticks(rotation=55)
plt.show()


data['lead_time'].hist()
plt.show()



sns.countplot(x='arrival_date_year',data=data)
plt.show()



arrival_per_year = data['arrival_date_year'].value_counts().sort_index()
sns.lineplot(x=arrival_per_year.index,y=arrival_per_year.values,color = 'violet')
plt.show()


sns.barplot(x=arrival_per_year.index,y=arrival_per_year.values)
plt.show()




arrival_per_month = data['arrival_date_month'].value_counts().sort_index()
sns.lineplot(x=arrival_per_month.index,y=arrival_per_month.values,color='green')
plt.show()


info_month = sns.countplot(x='arrival_date_month',data=data)

for info in info_month.containers:
    info_month.bar_label(info)
plt.show()


print(data['is_canceled'].value_counts())


canceled = sns.countplot(x='is_canceled',data=data)
for info in canceled.containers:
    canceled.bar_label(info)
plt.show()



canceled_time = data[data['is_canceled']==1]

sns.histplot(canceled_time['lead_time'],bins=20)
plt.show()

sns.boxplot(x=canceled_time['lead_time'])
plt.show()


guests_info = data[['adults','children','babies']]
sns.barplot(data = guests_info,palette='Set3')
plt.show()


print(data['customer_type'].unique())

guest_type=sns.countplot(x='customer_type',data=data)
for info in guest_type.containers:
    guest_type.bar_label(info)
plt.show()



print(data['reserved_room_type'].unique())
roomtype = sns.countplot(x='reserved_room_type',data=data,color='green')
for info in roomtype.containers:
    roomtype.bar_label(info)
plt.xlabel('Room types')
plt.ylabel('Number of rooms')
plt.show()




print(data['assigned_room_type'].unique())
assigned_roomtype = sns.countplot(x='assigned_room_type',data=data,color='green')
for info in assigned_roomtype.containers:
    assigned_roomtype.bar_label(info)
plt.xlabel('Assigned Room types')
plt.ylabel('Number of rooms')
plt.show()




sns.barplot(x='reserved_room_type',y='booking_changes',data=data,color='green')
plt.title('Relationship between Room types and Booking changes')
plt.xlabel('Room type')
plt.ylabel('Booking changes')
plt.show()


sns.barplot(x='meal',y='adr',data=data,color='violet')
plt.title('Realtiosnhip between meal types and daily average rate')
plt.xlabel('Meal types')
plt.ylabel('Average daily rate')
plt.show()

print(data.columns)


sns.barplot(x='total_of_special_requests',y='adr',data=data)
plt.title('Relationship between total of special requests and average daily rate')
plt.xlabel('total of special requests')
plt.ylabel('Average daily rate')
plt.show()



print(data['country'].unique())


countries_sort = data['country'].value_counts().nlargest(6).index
top_countries =data[data['country'].isin(countries_sort)]

sns.countplot(x='country',data=top_countries,order=countries_sort)
plt.show()

print(data['market_segment'].unique())
market_info = data['market_segment'].value_counts().index


market_segment_ordered = data[data['market_segment'].isin(market_info)]
market_sns = sns.countplot(x='market_segment',data=market_segment_ordered,order=market_info)
for info in market_sns.containers:
    market_sns.bar_label(info)

plt.show()

numerical_cols = data.select_dtypes(include='number')
corr1 = numerical_cols.corr()
sns.heatmap(corr1,annot=True)
plt.show()

data['arrival_date']=pd.to_datetime(data[['arrival_date_year','arrival_date_month','arrival_date_day_of_month']].astype('str').agg('-'.join,axis=1))
bookings_over_time = data.groupby('arrival_date').size().reset_index(name='num_bookings')
sns.lineplot(x='arrival_date',y='num_bookings',data=bookings_over_time)
plt.show()



data['date_arrival_info'] = pd.to_datetime(data[['arrival_date_year','arrival_date_month','arrival_date_day_of_month']].astype('str').agg('-'.join,axis=1))
data['day_of_week'] = data['date_arrival_info'].dt.day_name()
sns.barplot(x='day_of_week',y='is_canceled',data=data,palette='viridis')
plt.show()



different_room_types = data[data['reserved_room_type']!=data['assigned_room_type']]
sns.countplot(x='reserved_room_type',data=different_room_types,hue='assigned_room_type')
plt.legend(title='Assigned room type',title_fontsize=10)
plt.show()




data = data.dropna()














