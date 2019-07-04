import re
# 要让正则表达式不区分大小写，可以向 re.compile 传入re.IGNORECASE 或 re.I

robocop = re.compile(r'robocop',re.I)
mo = robocop.search('RoboCop is part man,part machine,all cop')
print(mo.group())

mo1 = robocop.search('ROBOCOP is part man,part machine,all cop')
print(mo1.group())

mo2 = robocop.search('AI,why does your programming book talk about robocop so much?')
print(mo2.group())