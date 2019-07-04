import requests

# 一行 get 请求
#r = requests.get('https://api.github.com/events')

# 一行 post 请求

#r = requests.pose('https://httpbin.org/post', data = {'key':'value'})

# 其他 http 请求

# 假装自己是浏览器
#url = 'https://api.gethub.com/some/endpoint'

#hreaders = {'user-agent': 'my-app/0.0.1'}

#r = requests.get(url, headers=headers)

# 获取服务器响应文本内容
#q = requests.get('https://api.github.com/events')
#print(q.text)

# 获取响应码
#w = requests.get('https://httpbin.org/get')
# print(w.status_code)

# 获取响应头
# print(w.headers)
# 获取Json 响应内容
# print(w.json())

# 获取 socket 响应内容
#r = requests.get('https://api.github.com/events', stream=True)
# print(r.raw)
#print(r.raw.read(10))

# post 请求
# 当想要一个键添加多个值的时候
#payload_tuples = [('key1','value1'),('key1','value2')]
#r1 = requests.post('https://httpbin.org/post',data=payload_tuples)
#payload_dict = {'key1':['value1','value2']}
#r2 =requests.post('https://httpbin.org/post',data=payload_dict)
# print(r1.text == r2.text)

#请求的时候用 Json 作为参数
#url = 'https://api.github.com/some/endpoint'
#pyload = {'some':'data'}
#r = requests.post(url,json=pyload)

# 上传文件
#url = 'https://httpbin.org/post'
#files = {'file':open('report.xls','rb')}
#r =requests.post(url,files=files)
#print(r.text)



# 获取 cookie 信息
#url = 'http://example.com/some/cookie/setting/url'
#r = requests.get(url)
#r.cookies['example_cookie_name']


# 发送cookie 信息
#url = 'https://httpbin.org/cookies'
#cookies = dict(cookies_are='working')
#r = requests.get(url,cookies=cookies)
#print(r.text)

# 设置超时
requests.get('https://github.com/',timeout=0.001)