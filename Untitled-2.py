# coding: utf-8
import time
import pandas as pd
import os
from selenium import webdriver
from bs4 import BeautifulSoup


url ="https://qiita.com"
driver = webdriver.Chrome("C:\\Users\\shunkoiso\\Desktop\\VSCode\\chromedriver.exe")

# ページにアクセス
driver.get(url)

# 検索ボックスを見つけてキーワードを検索
search = driver.find_element_by_class_name("st-Header_searchInput")
search.send_keys("python")
search.submit()
time.sleep(5)

# 検索先のページのHTMLを取得
html = driver.page_source.encode('utf-8')
soup = BeautifulSoup(html, 'lxml')

# 実行ファイルの絶対パスを取得し、そのファイルパスのディレクトリパスを取得する
output_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "out.csv"
# output_dirとfile_nameを結合したパスを作成する
output_file = os.path.join(output_dir,file_name)

# 結果を出力 # 出力ファイルをオープンする
#witn open(output_file, mode='w', encoding='utf-8', newline="\r\n") as f:
f = open(output_file, mode='w', encoding='utf-8')
results = soup.find_all("h1", class_="searchResult_itemTitle")
for result in results:
    href = result.findAll("a")[0].get("href")
    f.write(url + href)
    f.write('\r\n')

driver.close()
driver.quit()