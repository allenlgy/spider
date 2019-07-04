import re
# *意味着“匹配零次或多次”，星号之前的分组可以在文本中出现任意次
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventure of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventure of Batwoman')
print(mo2.group())

mo3 = batRegex.search('The Adventure of Batwowowoman')
print(mo3.group())