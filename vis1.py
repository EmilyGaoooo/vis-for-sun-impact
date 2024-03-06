import matplotlib.pyplot as plt
import pandas as pd

df_excel = pd.read_excel('D:/5120/dataset/final/combined_data.xlsx')

fig, ax1 = plt.subplots(figsize=(14, 8))

width = 0.35
ax1.bar(df_excel['Year'], df_excel['Count_incidence'], width, label='Count Incidence', color='skyblue')
ax1.set_xlabel('Year')
ax1.set_ylabel('Count Incidence')
ax1.tick_params(axis='y')

ax2 = ax1.twinx()
ax2.plot(df_excel['Year'], df_excel['incidence_rate'], label='Incidence Rate', color='blue', marker='o')
ax2.set_ylabel('Rate (per 100,000)')
ax2.tick_params(axis='y')

ax3 = ax1.twinx()
ax3.plot(df_excel['Year'], df_excel['Avg_UV Index'], label='Avg_UV Index', color='green', marker='s')
ax3.set_ylabel('Avg_UV Index')

ax3.spines.right.set_position(('outward', 60))
ax3.tick_params(axis='y', labelcolor='green')

plt.title('Count of Incidence, Incidence Rate, and UV Index over Years')
ax1.legend(loc='upper left')
ax2.legend(loc='lower left')
ax3.legend(loc='upper right')

plt.show()
