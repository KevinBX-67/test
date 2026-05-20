import numpy as np
import pandas as pd


# =====================================================================
# 步驟 1: 自動生成「SuperMarket Analysis.csv」測試檔案
# (這樣你不用擔心找不到檔案，程式會自動幫你放進 PyCharm 當前目錄中)
# =====================================================================
def generate_mock_data():
    np.random.seed(42)
    n_rows = 500

    branches = ["A", "B", "C"]
    cities = ["Yangon", "Naypyitaw", "Mandalay"]
    cust_types = ["Member", "Normal"]
    genders = ["Female", "Male"]
    product_lines = [
        "Electronic accessories",
        "Fashion accessories",
        "Food and beverages",
        "Health and beauty",
        "Home and lifestyle",
        "Sports and travel",
    ]

    mock_data = {
        "Invoice ID": [f"{i:03d}-{i:02d}" for i in range(n_rows)],
        "Branch": np.random.choice(branches, n_rows),
        "City": np.random.choice(cities, n_rows),
        "Customer type": np.random.choice(cust_types, n_rows),
        "Gender": np.random.choice(genders, n_rows),
        "Product line": np.random.choice(product_lines, n_rows),
        "Unit price": np.random.uniform(10, 100, n_rows),
        "Quantity": np.random.randint(1, 10, n_rows),
        "Total": np.random.uniform(50, 800, n_rows),  # Kaggle 的總銷售額欄位
        "Rating": np.random.uniform(4, 10, n_rows),
    }

    df_gen = pd.DataFrame(mock_data)
    # 將生成的資料匯出為指定的檔名
    df_gen.to_csv("SuperMarket Analysis.csv", index=False, encoding="utf-8")
    print("【系統提示】已在當前目錄自動生成 'SuperMarket Analysis.csv' 檔案！\n")


# 執行生成檔案函式
generate_mock_data()


# =====================================================================
# 步驟 2: 電商資料分析實例操作
# =====================================================================

# 1. 讀取資料
file_path = "SuperMarket Analysis.csv"
df = pd.read_csv(file_path)

# 將 Kaggle 中的總金額欄位 'Total' 重新命名為題目指定的 'Sales' 以利後續分析
if "Total" in df.columns and "Sales" not in df.columns:
    df = df.rename(columns={"Total": "Sales"})

# [檢視] 檢視資料筆數與前幾筆內容
print("=== 原始資料檢視 ===")
print(f"資料總筆數：{df.shape[0]} 筆，欄位數：{df.shape[1]} 欄")
print("前 5 筆資料內容：")
print(df.head(5))
print("-" * 60)


# 2. [篩選] 篩選出 Branch 為 A 且 Customer type 為 Member 的交易資料
condition = (df["Branch"] == "A") & (df["Customer type"] == "Member")
df_filtered = df[condition]

print("=== 條件篩選結果 ===")
print(f"符合條件（Branch 為 A 且為 Member 會員）的交易筆數：{df_filtered.shape[0]} 筆")
print("-" * 60)


# 3. [聚合] 以 Product line 為單位，計算各產品線的 總銷售額(Sales) 與 平均評分(Rating)
# 使用 round(2) 計算至小數後 2 位
prod_summary = (
    df_filtered.groupby("Product line")
    .agg(Sales_Sum=("Sales", "sum"), Rating_Avg=("Rating", "mean"))
    .round(2)
)

# 重新命名欄位名稱
prod_summary.columns = ["總銷售額 (Sales)", "平均評分 (Rating)"]

print("=== 各產品線銷售與評分彙總 ===")
print(prod_summary)
print("-" * 60)


# 4. [分組] 依 City 與 Gender 分組，計算平均銷售額與交易筆數
city_gender_summary = (
    df_filtered.groupby(["City", "Gender"])
    .agg(Sales_Avg=("Sales", "mean"), Transaction_Count=("Sales", "count"))
    .round(2)
)

city_gender_summary.columns = ["平均銷售額", "交易筆數"]

print("=== 依城市與性別分組之統計 ===")
print(city_gender_summary)
print("-" * 60)


# 5. [結論] 找出總銷售額最高的產品線
top_product_line = prod_summary["總銷售額 (Sales)"].idxmax()
top_sales_amount = prod_summary["總銷售額 (Sales)"].max()

print("=== 關鍵指標結論 ===")
print(f"🏆 總銷售額最高的產品線為：【{top_product_line}】")
print(f"   其總銷售金額為：${top_sales_amount:,.2f}")
print("-" * 60)


# 6. [匯出] 將各產品線的銷售與評分彙總結果輸出為 0520_pandas_3OK.CSV 檔案
prod_summary.to_csv("0520_pandas_3OK.CSV", encoding="utf-8-sig")
print("💾 統計結果已成功輸出至檔案：0520_pandas_3OK.CSV")