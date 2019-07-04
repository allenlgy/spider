import re
# 字符|称为“管道”。 希望匹配许多表达式中的一个时，就可以使用
heroRegex = re.compile(r'Batman|Tina Fey')

mo1 = heroRegex.search('Batman and Tina Fey.')

print(mo1.group())  # 如果都出现在被查找的字符串中，第一次出现的匹配文本将作为Match对象

mo2 = heroRegex.search('Tina Fey and Batman')

print(mo2.group())

# 也可以使用管道来匹配多个模式中的一个，作为正则表达式的一部分。
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())

print(mo.group(1))