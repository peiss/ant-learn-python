# pip install requests
import requests

# 发送get请求获取URL返回结果
r = requests.get('http://www.baidu.com')
# 发送post请求获取URL的返回结果
r = requests.post(
    'http://xxx.org/post',
    data={'key': 'value'}
)

# 查看返回状态码，如果==200代表访问成功
r.status_code

# 获取返回的网页内容
r.text
