import pandas as pd

# 1. 先用 list 建立原始資料，並使用 pandas 建立 stock1 (預設索引)
data = [120, 80, None, 60, 95, None, 110]
stock1 = pd.Series(data)

# 2. 加入指定的水果名稱作為索引，建立 stock2
index_labels = ['Apple', 'Banana', 'Orange', 'Mango', 'Grape', 'Peach', 'Melon']
stock2 = pd.Series(data, index=index_labels)

# 3. 將 stock2 轉換為字典 (dict) 格式的 stock3
stock3 = stock2.to_dict()

# 4. 依題目要求輸出各項結果
print("stock1")
print(stock1)
print()

print("stock2")
print(stock2)
print()

print("stock3")
print(stock3)
print()

print("Banana 的庫存值")
print(stock2['Banana'])
print()

print("計算缺失值")
# 使用 .isnull().sum() 計算 Series 中有多少個 NaN (None)
print(stock2.isnull().sum())

# 5. 把 stock2 存檔為 0520_stock.csv
# 由於輸出範例只有索引與數值，存檔時可設定 header=False 不寫入欄位名稱
stock2.to_csv('0520_stock.csv', header=False)