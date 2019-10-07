import time

def spider_url(url):
    print("spider url:", url)
    time.sleep(2)

if __name__ == "__main__":
    todo_urls = ["http://www.url%d.com"%i for i in range(100)]
    for url in todo_urls:
        spider_url(url)