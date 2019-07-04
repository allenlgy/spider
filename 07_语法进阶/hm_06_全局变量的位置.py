# 注意： 在开发时， 应该把模块中的所有全局变量
# 定义在所有函数的上方
# 使所有函数都能正常访问变量
gl_num = 10
gl_name = "xiaoming"
gl_title = "黑马程序员"

def demo():

    num = 90

    print("%d" %num)
    print("%s" % gl_title)
    print("%s" % gl_name)

# 再定义一个全局变量


demo()


# 再定义一个全局变量
# name = "小明"