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

    # 子类拥有父类所有的属性和方法
    # def eat(self):
    #     print("吃")
    #
    # def drink(self):
    #     print("喝 ")
    #
    # def run(self):
    #     print("跑")
    #
    # def sleep(self):
    #     print("睡")

    def bark(self):
        print("wangwang")


# 创建一个对象 - 狗
wangcai = Dog()

wangcai.eat()
wangcai.run()
wangcai.drink()
wangcai.sleep()
wangcai.bark()
