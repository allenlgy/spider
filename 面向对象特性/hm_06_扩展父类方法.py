class Animal:

    def eat(self):
        print("吃")

    def drink(self):
        print("喝 ")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")

class Dog(Animal):

    def bark(self):
        print("wangwang")

class XiaoTianQuan(Dog):

    def fly(self):
        print("fei")

    def bark(self):

        # 1. 针对子类特有的需求编写代码
        print("神叫")

        # 2. 使用 super(). 调用原本在父类的方法
        # super().bark()
        # 注意不能用子类调用方法，会出现递归调用，死循环

        # 父类名.方法(self)
        Dog.bark(self)

        # 3. 增加其他子类的代码
        print("!@#!@$!")
xtq = XiaoTianQuan()
# 如果子类中，重写了父类的方法
# 在使用子类对象调用方法时，会使用子类的方法
xtq.bark()