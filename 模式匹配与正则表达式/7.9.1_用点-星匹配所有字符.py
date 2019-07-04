import re
# 可以用点星表示任意文本（.*）
# .表示‘除换行符外所有单个字符’ * 表示匹配零次或者多次

nameRegex = re.compile(r'First Name:(.*) Last Name:(.*)')
mo = nameRegex.search('First Name: AI Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))


# 默认贪心匹配。加个问号改为非贪心匹配

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner')
print(mo.group())