class Women:

    def __init__(self, name):

        # 双下划线表示私有属性，外部不能随意访问
        self.name = name
        self.__age = 18

    def __secret(self):

        # 在对象方法内部，同样可以访问私有属性
        print("%s的年龄是 %d" % (self.name, self.__age))


xiaofang = Women("小芳")

# 伪私有属性不允许外界访问
print(xiaofang._Women__age)
# 私有方法同样不允许外界直接访问
xiaofang._Women__secret()

# 这种访问不建议
