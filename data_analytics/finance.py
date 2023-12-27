import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('data_analytics/finance.csv')
'''
mean1 = data['Market Cap(in B USD)'].mean()
med1 = data['Market Cap(in B USD)'].median()
std1 = data['Market Cap(in B USD)'].std()
print('Mean value for market cap is {}'.format(mean1))
print('median for Market Cap is {}'.format(med1))
print('Standart deviation for Market Cap is {}'.format(std1))
print('-----------------------------------------------------')
mean2 = data['Revenue'].mean()
med2 = data['Revenue'].median()
std2 = data['Revenue'].std()
print('Mean value for revenueis {}'.format(mean2))
print('median for revenue is {}'.format(med2))
print('Standart deviation for revenue is {}'.format(std2))



high1 = data.sort_values(by='Market Cap(in B USD)').head(1)['Company '].values[0]
low1 = data.sort_values(by='Market Cap(in B USD)').tail(1)['Company '].values[0]
print('The highest and lowest companies according to rayting for Market Cap are ({},{})'.format(high1,low1))

high2 = data.sort_values(by='Revenue').head(1)['Company '].values[0]
tail2 = data.sort_values(by='Revenue').tail(1)['Company '].values[0]
print('The highest and lowest companies according to rayting for revenue are ({},{})'.format(high2,tail2))


high3 = data.sort_values(by='Net Income').head(1)['Company '].values[0]
tail3 = data.sort_values(by='Revenue').tail(1)['Company '].values[0]
print('The highest and lowest companies according to rayting for net income are ({},{})'.format(high3,tail3))



year1 = data.groupby('Year')['Revenue'].mean().head(1)
year2 = data.groupby('Year')['Revenue'].mean().tail(1)
year3 = data.groupby('Year')['Net Income'].mean().head(1)
year4 = data.groupby('Year')['Net Income'].mean().tail(1)
print('The year with the highest average for Revenue is {}'.format(year1))
print('The year with the lowest average for Revenue is {}'.format(year2))
print('The year with the highest average for Net income is {}'.format(year3))
print('The year with the lowest average for Net income is {}'.format(year4))


avg_year_for_cap = data.groupby('Year')['Market Cap(in B USD)'].mean()
avg_year_for_cap.plot(kind = 'line',color='red')
plt.title('Distribution of Average cap for years')
plt.xlabel('Year')
plt.ylabel('Average Cap')
plt.grid(True)
plt.show()


print(data['Category'].value_counts())




avg1 = data.groupby('Category')['Revenue'].mean()
avg1.plot(color='green')
plt.title('Average Revenue for each Category')
plt.xlabel('Category')
plt.ylabel('Average Revenue')
plt.show()
avg2 = data.groupby('Category')['Net Income'].mean()
avg2.plot(kind='line',color = 'green')
plt.title('Average Net Income for each Category')
plt.xlabel('Category')
plt.ylabel('Average Net Income')
plt.show()
avg3 = data.groupby('Category')['Market Cap(in B USD)'].mean()
avg3.plot(kind='line',color='blue')
plt.title('Average Market Cap for each Category')
plt.show()



info1 = data.sort_values(by='Debt/Equity Ratio').head(1)['Company '].values[0]
info2 = data.sort_values(by='Debt/Equity Ratio').tail(1)['Company '].values[0]
info3 = data.sort_values(by='Net Income').head(1)['Company '].values[0]
info4 = data.sort_values(by='Net Income').tail(1)['Company '].values[0]
info5 = data.sort_values(by='ROE').head(1)['Company '].values[0]
info6 = data.sort_values(by='ROE').tail(1)['Company '].values[0]
print('Company with the highest debt/equity ratio is {}'.format(info1))
print('Company with the lowest debt/equity ratio is {}'.format(info2))
print('Company with the highest net income  is {}'.format(info3))
print('Company with the lowest net income  is {}'.format(info4))
print('Company with the highest ROE  is {}'.format(info5))
print('Company with the lowest ROE  is {}'.format(info6))



arr = data['Debt/Equity Ratio'].corr(data['ROE'])
print(arr)

plt.scatter(data['Debt/Equity Ratio'],data['ROE'],alpha=0.7)
plt.title('Scatterplot between Debt/Equity ratio and ROE')
plt.show()


print('Company with the highest Profit margin-{}'.format(info_companies))
print('Company with the lowest Profit margin-{}'.format(info_companies2))

if corr1:
    print(corr1)
else:
    print('There is not correleation between 2 columns')
    
print(data['Free Cash Flow Yield'].head(2))


highest_cash_flow = data.sort_values(by='Cash Flow from Operating').head(5)
print(highest_cash_flow)
lowest_cash_flow = data.sort_values(by='Cash Flow from Operating').tail(5)
print(lowest_cash_flow)

highest_company = highest_cash_flow['Company '].values
highest_cash = highest_cash_flow['Cash Flow from Operating'].values
plt.bar(highest_company,highest_cash,color='green')
plt.title('Highest cash flow among countries')
plt.xlabel('Companies')
plt.ylabel('Cash Flow')
plt.grid(True)
plt.show()

lowest_company = lowest_cash_flow['Company '].values
lowest_cash = lowest_cash_flow['Cash Flow from Operating'].values
plt.barh(lowest_company,lowest_cash,color='blue')
plt.title('Lowest cash flow among countries')
plt.ylabel('Companies')
plt.xlabel('Cash Flow')
plt.show()

corr2 = data['Inflation Rate(in US)'].corr(data['Profit Margin per Employee'])
print(corr2)
corr3 = data['Inflation Rate(in US)'].corr(data['ROE'])
print(corr3)

plt.scatter(data['Inflation Rate(in US)'],data['ROE'],alpha=0.8)
plt.show()

corr4 = data['Inflation Rate(in US)'].corr(data['Cash Flow from Operating'])
print(corr4)



metrics = ['Revenue', 'Net Income', 'EBITDA']
fig,axes = plt.subplots(nrows = len(metrics),ncols = 1,sharex=True)
for idx,metric in enumerate(metrics):
    axes[idx].plot(selected_company['Year'],selected_company[metric],marker = 'o',color='violet')
    axes[idx].set_title('Yearly {} for Google'.format(metric))
    axes[idx].set_title(metric)
axes[idx].set_xlabel('Year')
plt.show()


sorted_data = selected_company.sort_values(by='Year')
years = 5
beginning = sorted_data.iloc[0]['Market Cap(in B USD)']
ending = sorted_data.iloc[-1]['Market Cap(in B USD)']
cagr = ((ending/beginning)**(1/years))-1
print(f'The compounded growth rate of Google of market cap for 5 years is{cagr:.2%}')
'''

data['Profit Margin per Employee']=data['Net Profit Margin']/data['Number of Employees']
info_companies = data.sort_values(by='Profit Margin per Employee').head(1)['Company '].values[0]
info_companies2 = data.sort_values(by='Profit Margin per Employee').tail(1)['Company '].values[0]
data['Free Cash Flow Yield'] = (data['Free Cash Flow per Share'] / data['Earning Per Share'])*100
corr1 = data['Number of Employees'].corr(data['Earning Per Share'])
selected_company = data[data['Company ']=='GOOG']


avg_data = data.groupby('Category').agg({
    'ROE':'mean',
    'ROA':'mean',
    'Net Profit Margin':'mean'
}).reset_index()
print(avg_data)
arr = ['ROE','ROA','Net Profit Margin']
for i in arr:
    plt.bar(avg_data['Category'],avg_data[i],label=i)
plt.xlabel('Category')
plt.ylabel('Average Value')
plt.legend()
plt.show()














