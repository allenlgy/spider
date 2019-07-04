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

# 创建一个对象
xtq = XiaoTianQuan()
xtq.fly()
xtq.bark()
xtq.sleep()