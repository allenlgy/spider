import re
# 正则表达式不仅可以查找，还可以替换查找到的字符
# sub() 方法传入 两个参数，第一个用于取代的字符串，第二个匹配的内容。

namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED','Agent Alice gave the secret documents to Agent Bob')

# 假设要隐去密探的姓名，只显示第一个字母
agentNamesRegex = re.compile(r'Agent (\w)\w*')
mo = agentNamesRegex.sub(r'\1****','Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(mo)