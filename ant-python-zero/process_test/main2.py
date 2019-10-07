import time
import multiprocessing

def spider_url(url):
    print("spider url:", url)
    time.sleep(2)

if __name__ == "__main__":
    todo_urls = ["http://www.url%d.com"%i for i in range(100)]
    with multiprocessing.Pool() as pool:
        pool.map(spider_url, todo_urls)