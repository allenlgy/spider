import re
# 可以用方括号定义自己的字符分类
vowelRegex = re.compile(r'[aeiouAEIOU]')
mo = vowelRegex.findall('RoboCop eats baby food . BABY FOOD')
print(mo)

# 在方括号的正则式表达符号不会被解释，不需要在前面加到斜杠转义
# 在字符分类的左方括号后加上字符^,就可以得到“非字符类”
consonantRegex = re.compile(r'[^aeiouAEIOU]')
mo1 = consonantRegex.findall('RoboCop eats baby food . BABY FOOD')
print(mo1) # 现在是匹配所有非元音字母