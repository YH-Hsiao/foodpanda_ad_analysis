import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

# 設定中文字型
font_path = "C:/Windows/Fonts/msjh.ttc"  # 微軟正黑體字型路徑
font_prop = font_manager.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()


# 讀取資料
df = pd.read_csv('data/foodpanda_sales.csv')

# 計算每個廣告渠道的總營收和總花費
channel_summary = df.groupby('MarketingChannel').agg({
    'Revenue': 'sum',
    'MarketingCost': 'sum'
}).reset_index()

# 計算 ROAS（營收/花費）
channel_summary['ROAS'] = channel_summary['Revenue'] / channel_summary['MarketingCost']

# 依 ROAS 排序
channel_summary = channel_summary.sort_values('ROAS', ascending=False)

# 繪製長條圖
plt.bar(channel_summary['MarketingChannel'], channel_summary['ROAS'])
plt.title('Foodpanda 各廣告渠道 ROAS')
plt.xlabel('廣告渠道')
plt.ylabel('ROAS')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('dashboard/roas_by_channel.png')  # 存圖
plt.show()
