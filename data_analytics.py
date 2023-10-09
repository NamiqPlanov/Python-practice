import pandas as pd
import mattplotlib.pyplot as plt
import seaborn as sns

fifa = pd.read_csv('fifa_data.csv')
fifa.head()
fifa.shape
for col in fifa.columns:
    print(col)
fifa['nationality'].value_counts()
fifa['nationality'].value_counts()[0:5]
fifa['nationality'].value_counts()[0:5].keys()

fifa.figuresize(fgsize=(8,7))
fifa.bar(list(fifa['nationality'].value_counts()[0:5].keys()),list(fifa['nationality'].value_counts()[0:5].keys()),color ='blue' )
fifa.show()

player_salary = fifa[['short_name','euro_wage']]
player_salary.head()
player_salary = player_salary.sort_values(by=['wage_euro'],ascending = False)
player_salary.head()

plt.figure(fgsize = (8,6))
plt.bar(list(player_salary['short_name'].value_counts()[0:5]),list(player_salary['euro_wage'][0:5]),color='green')
plt.show()


