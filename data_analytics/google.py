import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from statsmodels.tsa.seasonal import seasonal_decompose


data = pd.read_csv('data_analytics/google.csv')
'''
print('is there any null values?{}'.format(data.isnull().values.any()))
print(data.describe())



data['Volume'].hist()
plt.title('Distribution of volumes')
plt.xlabel('Volume')
plt.ylabel('Amount')
plt.show()


data.set_index('Date',inplace=True)

plt.plot(data['Open'],label='Open',linewidth=3)
plt.plot(data['Close'],label='Close',linewidth=3)
plt.plot(data['High'],label='Hight',linewidth=3)
plt.plot(data['Low'],label='Low',linewidth=3)
plt.show()



data.set_index('Date',inplace=True)
plt.plot(data['Close'],label='Close Price')
plt.xlabel('Year')
plt.ylabel('Close Prices')
plt.legend()
plt.show()

result = seasonal_decompose(data['Close'],model='additive',period=1)

plt.plot(data['Close'],label='Close')
plt.legend()

plt.plot(result.seasonal,label='Seasonal')
plt.legend()

plt.plot(result.trend,label='Trends')
plt.legend()

plt.plot(result.resid,label='Residual Component')
plt.legend()

plt.tight_layout()
plt.show()



data = data.dropna()
print(data.head(1))


data['Daily Price Changes'].hist(bins=15,color='green')
plt.title('Distribution of Daily Price Changes')
plt.show()


plt.plot(data['Date'],data['Close'],label='Close Prices')
plt.plot(data['Date'],data['Day 50'],label='Moving Averages for 50 days')
plt.plot(data['Date'],data['Day 10'],label='Moving Averages for 10 days')
plt.title('Stock Prices and Moving Averages')
plt.show()

print(data.corr())

sns.heatmap(data.corr())
plt.show()

sns.scatterplot(x='Volume',y='Close',data=data)
plt.title('Relationship between trading volume and Close price')
plt.show()


figure = go.Figure()
figure.add_trace(go.Candlestick(
    x=data['Date'],
    open = data['Open'],
    low = data['Low'],
    close = data['Close'],
    high = data['High'],
    name='Candlestick')

)
figure.show()


data['Close'].hist(bins=16)
plt.show()



lag_periods = int(input('how many lag periods:'))

for i in range(1,lag_periods+1):
    data[f'Close log {i}'] = data['Close'].shift(i)

print(data.head(4))
'''
data['Date'] = pd.to_datetime(data['Date'])

data['Daily Price Changes'] = data['Close'].pct_change()*100

data.sort_values('Date',inplace=True)

data['Day 50'] = data['Close'].rolling(window=50,min_periods=1).mean()
data['Day 10'] = data['Close'].rolling(window=10,min_periods=1).mean()




print(data.columns)

events = [{
    'date':'2021-05-19',
    'event':'Neftchi vs Qarabag match'
},{
    'date':'2021-08-19',
    'event':'Neftchi vs Maccabi Haifa match'
}]

for event in events:
    event['date'] = pd.to_datetime(event['date'])

plt.plot(data['Date'],data['Close'],label='Close Price')
for event in events:
    plt.axvline(x=event['date'],label=event['event'],color='green')
plt.title('Close prices for events')
plt.xlabel('dates')
plt.ylabel('Prices')
plt.legend()
plt.show()