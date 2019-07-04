import urllib.request
respone = urllib.request.urlopen("http://www.baidu.com")
print(respone.read().decode("utf-8"))

# request 的 urlopen方法，可以传入三个参数
# urllib.request.urlopen(url, data=None ,[timeout,]*)
# 第一个 url 就是请求的链接，像百度
# 第二个给 post 请求携带参数的，在这里用 byte 类型船体
# 第三个设置请求超时时间