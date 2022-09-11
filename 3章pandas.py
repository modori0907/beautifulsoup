import pandas as pd

df = pd.read_csv("test.csv")

# 1行のデータを表示
print("C is dat\n", df.loc[2])

# 複数の行のデータを表示
print("")


#1 ---
# CSVファイルの読み込み
#
# df = pd.read_csv("test.csv")
# print("number of data =", len(df))
# print("name           =", df.columns.values, type(df.columns.values))
# print("index          =", df.index.values)

#2 ---
# 列データ、行データを取得する
# 1列のデータを表示
# print("国語の列データ\n", df["国語"])
#
# # 複数の列のデータを表示
# print("国語と数学の列データ\n", df[["国語", "数学"]])
