import re
# 想要一个分组重复特定次数，在正则表达式后面跟花括号包围的数字
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())