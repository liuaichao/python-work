import pandas as pd

# data = pd.read_csv('./data/java.csv')
# # print(data.loc[:,'工作地点'].value_counts())
a = 0
for i in ['./data/Android.csv', './data/hadoop.csv']:
    data = pd.read_csv(i)
    data = data.loc[:,'工作地点']
    if '深圳' in data.values:
        a += 1
print(a)