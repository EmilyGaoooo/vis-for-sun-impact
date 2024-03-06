import pandas as pd
import matplotlib.pyplot as plt

df_excel = pd.read_excel('D:/5120/dataset/final/combined_data.xlsx')

# First Visualization: Year vs Avg_UV Index vs incidence_rate
fig, ax1 = plt.subplots(figsize=(14, 8))
ax1.set_xlabel('Year')
ax1.set_ylabel('Avg_UV Index', color='tab:red')
ax1.plot(df_excel['Year'], df_excel['Avg_UV Index'], color='tab:red', marker='o')
ax1.tick_params(axis='y', labelcolor='tab:red')
ax2 = ax1.twinx()
ax2.set_ylabel('Incidence Rate (per 100,000)', color='tab:blue')
ax2.plot(df_excel['Year'], df_excel['incidence_rate'], color='tab:blue', marker='x')
ax2.tick_params(axis='y', labelcolor='tab:blue')
plt.title('Year vs Avg_UV Index vs Incidence Rate')
plt.show()

