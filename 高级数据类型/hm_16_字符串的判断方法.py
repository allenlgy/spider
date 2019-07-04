# 1. 判断空白字符
space_str = ' \t\n\r'

print(space_str.isspace())


# 2.判断字符串是否只包含数字
# 都不能判断小数
# unicode 字符串
# num_str = "\u00b2"
# 中文数字
num_str = "一千零一"

print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())