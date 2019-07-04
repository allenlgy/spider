a = 6
b = 100

# 1使用其他变量
# c =a
# a = b
# b = c

# 2.不使用其他变量
# a = a + b
# b = a - b
# a = a - b


# 3 python 独有
# 等号右边是一个元组， 只是把括号省略
a, b = b, a

print(a)
print(b)