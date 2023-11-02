import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('data_analysis_tool/players_20.csv')
print('Data head:')
data.head()

summary = data.describe()
plt.figure(figsize=(5,5))
plt.bar(list(data['overall'].value_counts()[0:5].keys()),list(data['overall'].value_counts()[0:5]),color='blue')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
filtered_data = data[data['overall']>90]

summary.to_csv('info.csv',index=False)
filtered_data.to_csv('detailed.csv',index=False)