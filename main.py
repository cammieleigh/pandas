import pandas as pd
df = pd.read_csv('data/new1dictionary.csv')
df
df["Radical"].value_counts()
df["Pinyin"].value_counts()
radicalCount = df.Radical.value_counts().reset_index().rename(
           columns={'index': 'Radical', 0: 'count'})
newCount = radicalCount.nlargest(5, 'count', keep='all')
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.pie(newCount["count"], labels = newCount["Radical"])