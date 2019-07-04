import  re
# 点星将匹配除换行符以外的所有字符，通过传入re.DOTALL 作为re.compile() 的第二个参数
# 可以匹配所有字符

noNewlineRegex = re.compile('.*')
mo = noNewlineRegex.search('Serve the pubilc trust.\nProtect the innocent.\nUphold the law')
print(mo.group())

newlineRegex = re.compile('.*',re.DOTALL)
mo = newlineRegex.search('Serve the pubilc trust.\nProtect the innocent.\nUphold the law')
print(mo.group())