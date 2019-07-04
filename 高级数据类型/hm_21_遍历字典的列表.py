students = [
    {"name":"tu"},
    {"name":"mei"}
]

# 在学员列表中搜寻指定的姓名
find_name = "tu"

for students_dic in students:

    print(students_dic)

    if students_dic["name"] == find_name:

        print("zhaodaole %s" %find_name)

        # 退出循环
        break

else:
    # 如果希望在检查后没有这个元素的提示
    # 可以用 else

    print('meizhaodao %s' %find_name)