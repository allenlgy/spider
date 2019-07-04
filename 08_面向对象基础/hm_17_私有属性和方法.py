class Women:

    def __init__(self, name):

        # 双下划线表示私有属性，外部不能随意访问
        self.name = name
        self.__age = 18

    def __secret(self):

        # 在对象方法内部，同样可以访问私有属性
        print("%s的年龄是 %d" % (self.name, self.__age))


xiaofang = Women("小芳")

# print(xiaofang.age)
# 私有属性同样不允许外界直接访问
xiaofang.__secret()