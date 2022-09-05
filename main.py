import requests
from bs4 import BeautifulSoup
import urllib  # 「相対url」を「絶対url」に変換する

# Webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test2.html"

html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")  # html解析オブジェクト



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
#     link_url = urllib.parse.urljoin(load_url, url)  # 絶対urlを取得。相対URLの場合は変k擦る
#     print(link_url)
