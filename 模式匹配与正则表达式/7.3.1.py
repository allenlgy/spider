import re
phoneNumregex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
mo = phoneNumregex.search("My number is 415-555-4242")
areaCode,mainNumber = mo.groups()
print(mo.group())
print(areaCode)
"""
第一个括号用group（1）匹配，第二个用2来匹配
groups返回多个值的元组，可以使用多重赋值的技巧赋值给变量
"""
phoneNumregex = re.compile(r"(\(\d\d\d\)) (\d\d\d-\d\d\d)")
mo = phoneNumregex.search('My phone number is (415) 555-4242.')
print(mo.group())
