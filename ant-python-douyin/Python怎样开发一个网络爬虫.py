

# 这是下载网页的库
import requests

url = "http://www.crazyant.net"
r = requests.get(url)

# 这是爬取后的HTML
html = r.text

# 这是解析HTML的库
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'html.parser')
titles = [
    (article
     .find("h2", class_="entry-title")
     .find("a")
     .get_text()
     )
    for article
    in soup.find_all("article")
]

out_file = "./爬取结果.txt"
with open(out_file,
          "w",
          encoding="utf8") as fout:
    for title in titles:
        fout.write(title + "\n")
