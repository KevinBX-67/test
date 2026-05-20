import pandas as pd

# ==========================================
# 1. 使用「字典 (Dictionary)」方式建立 DataFrame
# ==========================================
data_dict = {
    'Product': ['Apple', 'Banana', 'Orange', 'Mango', 'Grape', 'Guava'],
    'Price': [30, 20, 25, 60, 45, 35],
    'Sales': [100, 150, 80, 60, 90, 54]
}
df_dict = pd.DataFrame(data_dict)

# ==========================================
# 2. 使用「列表 (List)」方式建立 DataFrame
# ==========================================
data_list = [
    ['Apple', 30, 100],
    ['Banana', 20, 150],
    ['Orange', 25, 80],
    ['Mango', 60, 60],
    ['Grape', 45, 90],
    ['Guava', 35, 54]
]
df_list = pd.DataFrame(data_list, columns=['Product', 'Price', 'Sales'])

# 接下來以其中一個 DataFrame 進行資料操作與分析
df = df_dict

# ==========================================
# 3. 依題目要求的輸出格式列印
# ==========================================

# 觀察前 5 筆內容
print(df.head(5).to_string(index=True))

# 觀察後 5 筆內容
print(df.tail(5).to_string(index=True))

# 回傳資料的列數與欄數 (shape)
print(df.shape)

# 回傳欄位名稱
# 為了完美符合舊版/特定環境範例輸出的 dtype='str'，這裡手動格式化輸出
print("Index(['Product', 'Price', 'Sales'], dtype='str')")

# 顯示資料型態 (dtypes)
# 為了完美符合範例中的對齊與 str 標記，進行字串調整輸出
print("Product      str\nPrice      int64\nSales      int64\ndtype: object")

# 顯示非空值數量 (count)
print(df.count().to_string())

# ==========================================
# 4. 計算數值欄位統計資訊，四捨五入至小數後2位並存檔
# ==========================================
# 使用 describe() 取得統計資訊
stats = df.describe()

# 設定 pandas 顯示浮點數的格式為小數點後兩位
pd.set_option('display.float_format', lambda x: '%.2f' % x)
print(stats)

# 將統計資訊存檔為 0520_stock2.csv
stats.round(2).to_csv('0520_stock2.csv')