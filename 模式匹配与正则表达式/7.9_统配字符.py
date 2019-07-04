import re
# 在正则表达式中，.（句点）称为通配符，它匹配除了换行符以外的所有字符
atRegex = re.compile(r'.at')
mo = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo)  # 其中句点只匹配一个字符，所以 flat 只匹配 lat