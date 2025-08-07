import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/foodpanda_sales.csv')

channel_summary = df.groupby('MarketingChannel').agg({
    'Revenue': 'sum',
    'MarketingCost': 'sum'
}).reset_index()
channel_summary['ROAS'] = channel_summary['Revenue'] / channel_summary['MarketingCost']

channel_summary = channel_summary.sort_values('ROAS', ascending=False)

plt.bar(channel_summary['MarketingChannel'], channel_summary['ROAS'])
plt.title('Foodpanda 各廣告渠道 ROAS')
plt.xlabel('廣告渠道')
plt.ylabel('ROAS')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('dashboard/roas_by_channel.png')
plt.show()
