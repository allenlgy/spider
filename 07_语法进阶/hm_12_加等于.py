def demo(num, num_list):

    print("函数开始")

    # 先相加再赋值，有了赋值不会对外部有影响
    num += num

    # 列表的 += 是相当于用 extend 的函数
    # 就可以对外部数据进行修改
    num_list += num_list

    # 想不修改可以这样写
    num_list = num_list + num_list

    print(num_list)

    print(num)

    print("函数完成")

gl_num = 9
gl_list = [1, 2, 3]
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)