# 注意： 定义：定义好函数之后，只表示这个函数封装了一段代码而已
# 如果不主动调用，函数不会自动执行

name = '小明'


def say_hello():
    '''
    打招呼
    :return:
    '''
    print('hello')
    print('hello')

# 只有在程序中，主动调用函数，才能执行函数
say_hello()

print(name)