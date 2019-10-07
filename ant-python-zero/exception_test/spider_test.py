"""
模拟爬虫，如果某个URL出了问题，不能影响其他正常URL的爬取
"""

urls = ["http://url1","http://url2","http://url3","http://url4"]


def spider_url(url):
    """
    爬取单个URL
    :param url:
    :return:
    """
    if "url2" in url:
        raise Exception("url return none:")
    return url+":success data"


def spider_urls(urls):
    """
    爬取多个URL的列表
    :param urls:
    :return:
    """
    for url in urls:
        print("\nbegin spider url: ", url)
        try:
            result = spider_url(url)
            print("spider success, result is:", result)
        except Exception as e:
            print("spider exception:",url)
            continue

spider_urls(urls)