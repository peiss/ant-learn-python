"""
模拟爬虫
爬取其中的一个URL有问题，不能影响其他的爬虫
"""


def spider_url(url):
    """
    爬取单个URL
    :param url:
    :return:
    """
    if "url2" in url:
        raise Exception("url spider return none.")
    return url + ", success data"


def spider_urls(urls):
    """
    爬取批量的URL
    :param urls:
    :return:
    """
    for url in urls:
        print("\nspider url:", url)
        try:
            result = spider_url(url)
            print("result is:", result)
        except Exception as e:
            print("spider url exception:", url, e)
            continue


spider_urls(["http://url1",
             "http://url2",
             "http://url3"])
