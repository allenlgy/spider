hello_str = "hello world"

# 1. 判断是否以指定字符开始
print(hello_str.startswith("H"))

# 2. 判断是否以指定字符串结束
print(hello_str.endswith("world"))

# 3. 查找指定字符
# index 同样能指定字符串位置
# find 方法如果找不到字符，不会报错，只会 -1
print(hello_str.find("llo"))
print(hello_str.find("abc"))

# 4. 替换字符串
# replace 方法执行完成之后形成一个新的字符串
# 不会修改原有的字符串

print(hello_str.replace("world","python"))

print(hello_str)
