name_list = ["zhangsan","lisi","wangwu"]

# 使用 del 关键字删除元素
# 日常开发中，建议使用列表的方法，尽量不用 del
del name_list[1]

# del 关键字本质上是将一个变量从内存中删除
name = "xiaoming"

del name
# del 会把变量从内存删除，后续代码就不能使用这个变量
print(name_list)