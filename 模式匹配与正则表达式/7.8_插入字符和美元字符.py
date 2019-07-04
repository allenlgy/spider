import re
# 在表达式前输入^字符表示从这里开始
beginWithHello = re.compile(r'^Hello')

beginWithHello.search('Hello World')

print(beginWithHello.search('He say no') == None)

# 在最后输入$字符表示从这里结束
endsWithNumber = re.compile(r'\d$')

endsWithNumber.search('Your number is 43')

print(endsWithNumber.search('your number is two') == None)

