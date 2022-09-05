from pathlib import Path  # フォルダにアクセスするためのパッケージ
from bs4 import BeautifulSoup
import urllib
import requests
import time  # アクセスする間隔を作るため




# -----  参照  ----- #

# load_url = "https://www.ymori.com/books/python2nen/test2.html"
# 1----
# #  タグで検索する方法。タグで複数している場合は最初にヒットしたタグのみ
# print(soup.find("title").text)  # textをつけるとタグは排除して文字列のみ表示
# print(soup.find("h2").text)

# # 2----
# for element in soup.find_all("li"):  # すべてのliタグを検索して、その文字列を表示する。
#     print(element.text)

# # 3----
# chap2 = soup.find(id="chap2") # idが「chap2」の範囲の要素を検索
# for element in chap2.find_all("li"): # idが「chap2」の中で、liタグの文字列を検索
#     print(element.text)
# class指定は_classで範囲の検索を行う

# 4----
# Webページを取得して解析する
# load_url = "https://news.yahoo.co.jp/categories/it"
# html = requests.get(load_url)
# soup = BeautifulSoup(html.content, "html.parser")  # html解析オブジェクト
#
# topic = soup.find(class_="sc-dzQEYZ iyvEdP topics") # classを取得
# for element in topic.find_all("a"):
#     print(element.text)

# 4----
# リンク一覧を取得する。タグの中身をgetで指定して取得する。相対urlであれば絶対urlに変換する
# for element in soup.find_all("a"):
#     print(element.text)
#     url = element.get("href")  #  href属性を取り出す
#     link_url = urllib.parse.urljoin(load_url, url)  # 絶対urlを取得。相対URLの場合は変換される
#     print(link_url)

# 5----
# 取得したデータをテキストに書き込む
# filename = "linklist.txt"  # ファイルを書き込むモードで開く
# with open(filename, "w") as f:
#  # 全てのaタグを検索、リンクを絶対URLで書き出す
#     for element in soup.find_all("a"):
#         url = element.get("href")
#         link_url = urllib.parse.urljoin(load_url, url)
#         f.write(element.text+"\n")
#         f.write(link_url+"\n")
#         f.write("\n")

# 6----
# Webページを取得して解析する
# image_url = "https://www.ymori.com/books/python2nen/sample1.png"
# imgdata = requests.get(image_url)
#
# filename = image_url.split("/")[-1]  # 「/」でリストに分割します。
#
# #  画像ファイルはバイナリーファイルなので、ファイルを開くときに「mode="wd"」
# with open(filename, mode="wb") as f:
#     f.write(imgdata.content)

# 7----
# 保存用フォルダを作成して、画像を作成したフォルダに保存する
# out_folder = Path("download")
# out_folder.mkdir(exist_ok=True)  # downloadフォルダを作成
#
# image_url = "https://www.ymori.com/books/python2nen/sample1.png"
# imgdata = requests.get(image_url)
#
# filename = image_url.split("/")[-1]  # 「/」でリストに分割します。
# out_path = out_folder.joinpath(filename)  # フォルダ内のファイルにアクセスするパスを作る
#
# #  画像ファイルはバイナリーファイルなので、ファイルを開くときに「mode="wd"」
# with open(out_path, mode="wb") as f:
#     f.write(imgdata.content)


# 8 ---
# htmlに存在するすべての画像ファイルのURLを表示する
# load_url = "https://www.ymori.com/books/python2nen/test2.html"
# html = requests.get(load_url)
# soup = BeautifulSoup(html.content, "html.parser")
#
# for element in soup.find_all("img"):  #  imgタグを検索
#     src = element.get("src")  # src属性を取得
#
#     # 絶対URLと、ファイルを表示する
#     image_url = urllib.parse.urljoin(load_url, src) # 絶対URLを取得
#     filename = image_url.split("/")[-1] # ファイル名を取得
#     print(image_url, ">>", filename)


# # 9 ---
# # ページ内の画像を一括ダウンロードするプログラム
# # webページを取得して解析する
# load_url = "https://www.ymori.com/books/python2nen/test2.html"
# html = requests.get(load_url)
# soup = BeautifulSoup(html.content, "html.parser")
#
# # 保存用フォルダを作る
# out_folder = Path("download2")
# out_folder.mkdir(exist_ok=True)
#
# # 全てのimgタグを検索し、リンクを取得する
# for element in soup.find_all("img"):
#     src = element.get("src")
#
#     # 絶対URLを使って、画像データを取得する
#     image_url = urllib.parse.urljoin(load_url, src)
#     imgdata = requests.get(image_url)
#
#     # URLから最後のファイル名を取り出して、保存フォルダ名をつなげる
#     filename = image_url.split("/")[-1]
#     out_path = out_folder.joinpath(filename)
#
#     # 画像データを、ファイルに書き出す
#     with open(out_path, mode="wb") as f:
#         f.write(imgdata.content)
#
#     # 1回アクセスしたので1秒待つ
#     time.sleep(1)
#
