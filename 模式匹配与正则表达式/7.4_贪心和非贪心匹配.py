import re
# 正则表达式默认贪心匹配
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')  # 非贪心模式
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())