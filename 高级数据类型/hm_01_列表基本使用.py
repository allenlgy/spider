name_list = ["zhangsan", "lise", "wangwu"]

# 1. 取值和索引
print(name_list[0])

# 知道数据的内容，想确定数据在列表的位置
print(name_list.index("lise"))

# 2. 修改
name_list[1] = "李四"

# 3. 增加
# append 可以向列表末尾添加一个数据
name_list.append("wangxiaoer")
# insert 可以在指定位置添加一个数据
name_list.insert(1, "xiaomeimei")
# 把另外一个列表的数据全部添加进列表的末尾
temp_list = ["sun","zhu","sha"]
name_list.extend(temp_list)

# 4. 删除
# 可以从列表删除指定的数据
name_list.remove("wangwu")
# pop 可以默认把列表最后一个元素删除
name_list.pop()
# 也可以指定删除位置的数据
name_list.pop(3)
# 清空列表数据
name_list.clear()


print(name_list)