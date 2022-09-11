import openpyxl

# ------- 変数一覧 ------- #
# 対象AES指定
AES = [
    {"AES_NO": 1, "host_name": "test1", "IP_ADDRESS": "1.1.1.1", "ID": "cust", "PW": "Tmasss"},
    {"AES_NO": 2, "host_name": "test1", "IP_ADDRESS": "2.2.2.2", "ID": "cust", "PW": "Tmasss"},
]
# ExcelのFile Name
File_Name = "sample.xlsx"
Sheet_name = "test_config"

# ---- 内部処理を行うため
# 対象AESを指定する
aes_i = 0
# excel記載処理で列を移動する処理
excel_i = 1

# ------- Excel ファイルを用意------- #
# 初期シート削除
wb = openpyxl.Workbook()
wb.remove(wb["Sheet"])
ws_new = wb.create_sheet(title=Sheet_name)

# ------- 各種処理 ------- #


"""
テスト
とりあえずこの流れでいけそう
あとは最初にホスト名を入れてわかるようにするか
"""

if AES:  # 指定したAESの数分だけ実行される
    if aes_i == 0:
        print(AES[int(f"{aes_i}")]["AES_NO"])
        print(AES[int(f"{aes_i}")]["IP_ADDRESS"])

        # 1つ目の設定項目取得
        items = ["Aconfig", "Bconfig", "Cconfig"]
        configitem = ["Aset", "Bset", "CSet"]

        # 辞書に変換する
        zipped = zip(items, configitem)
        dicts = dict(zipped)

        # 取得したデータを入力
        # １行目にホスト名を記載する
        ws_new[f"B{excel_i}"] = AES[int(f"{aes_i}")]["host_name"]
        excel_i += 1

        for k, v in dicts.items():
            ws_new[f"A{excel_i}"] = k
            ws_new[f"B{excel_i}"] = v
            excel_i += 1

        # ２つ目の設定項目取得

        # 項目と値をリストに入れる
        items = ["2Aconfig", "2Bconfig", "2Cconfig"]
        configitem = ["2Aset", "2Bset", "2Set"]

        # 辞書に変換する
        zipped = zip(items, configitem)
        dicts = dict(zipped)

        for k, v in dicts.items():
            ws_new[f"A{excel_i}"] = k
            ws_new[f"B{excel_i}"] = v
            excel_i += 1

        excel_i = 1
        aes_i += 1


    if aes_i == 1:
        # 取得したデータを入力
        # １行目にホスト名を記載する
        ws_new[f"C{excel_i}"] = AES[int(f"{aes_i}")]["host_name"]
        excel_i += 1

        print(AES[int(f"{aes_i}")]["AES_NO"])
        print(AES[int(f"{aes_i}")]["IP_ADDRESS"])

        # 1つ目の設定項目取得
        items = ["Aconfig", "Bconfig", "Cconfig"]
        configitem = ["AAset", "BBset", "CCSet"]

        # 辞書に変換する
        zipped = zip(items, configitem)
        dicts = dict(zipped)

        # 取得したデータを入力
        for v in dicts.values():
            ws_new[f"C{excel_i}"] = v
            excel_i += 1

        # ２つ目の設定項目取得

        # 項目と値をリストに入れる
        configitem = ["2AAset", "2BBset", "22Set"]

        # 辞書に変換する
        zipped = zip(items, configitem)
        dicts = dict(zipped)

        for v in dicts.values():
            ws_new[f"B{excel_i}"] = v
            excel_i += 1

        excel_i = 0
        aes_i += 1

# ------- Excelファイル　ファイル名を指定して保存 ------- #
wb.save(File_Name)

# if AES:
#     if aes_i == 0:
#
#         print(AES[int(f"{aes_i}")]["AES_NO"])
#         print(AES[int(f"{aes_i}")]["IP_ADDRESS"])
#         aes_i +=1
#
#
#
#     if aes_i == 1:
#         print(AES[int(f"{aes_i}")]["AES_NO"])
#         print(AES[int(f"{aes_i}")]["IP_ADDRESS"])
#         aes_i +=1
#


"""
複数のAESに対しての処理を全て自動化するのが結構大変
自動化したいので、辞書型にしてそれをトリガーにして何かできないか

"""

# 9/11 とりえあずエクセルの処理を色々できた
# 2台目以降の場合、指定変更する
# とりあえず１台ずつ更新する


"""
# エクセルを用意する
File_Name = "sample.xlsx"

# 項目と値をリストに入れる
items = ["Aconfig", "Bconfig", "Cconfig"]
configitem = ["Aset", "Bset", "CSet"]

# 辞書に変換する
zipped = zip(items, configitem)
dicts = dict(zipped)

# シートを作成する
sheet_name = "test_config"


# データを追記する
# AESを自動で追記していく処理にする　1台目ならaes_no == 1
i = 1
if aes_no == 1:
    for k, v in dicts.items():
        ws_new[f"A{i}"] = k
        ws_new[f"B{i}"] = v
        i += 1
elif aes_no == 2:
    for v in dicts.values():
        ws_new[f"C{i}"] = v
        i += 1



# 2週目

# 項目と値をリストに入れる
items = ["2Aconfig", "2Bconfig", "2Cconfig"]
configitem = ["2Aset", "2Bset", "2Set"]

# 辞書に変換する
zipped = zip(items, configitem)
dicts = dict(zipped)

# データを追記する
for k,v in dicts.items():
    ws_new[f"A{i}"] = k
    ws_new[f"B{i}"] = v
    i += 1

# 保存する処理
wb.save(File_Name)

"""
