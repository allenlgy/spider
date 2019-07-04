import re
# 加号匹配“一次或者多次”，至少出现一次
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventure of Batwoman')
print(mo1.group())

mo2 = batRegex.search('The Adventure of Batwowowoman')
print(mo2.group())

mo3 = batRegex.search('The Adventure of Batman')
mo3 == None