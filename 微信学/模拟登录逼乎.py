from urllib import request,parse
import ssl
context = ssl._create_unverified_context()

# 定义请求的 url 和 header

url = 'http://biihu.cc//account/ajax/login_process/'

headers = {
    # 假装自己是浏览器
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64)AppleWebKit/537.36(KHTML,like Gecko)Chrome/70.0.3538.77 Safari/537.36',
}

# 定义请求参数

dict = {
    'return_url':'https://biihu.cc/',
    'user_name':'1006547624@qq.com',
    'password':'linguiyi',
    '_post_type':'ajax'
}
# 把请求的参数转化为 byte
data = bytes(parse.urlencode(dict),'utf-8')

# 封装 request
req = request.Request(url,data=data,headers=headers,method='POST')
# 进行请求
response = request.urlopen(req,context=context)

print(response.read().decode('utf-8'))
