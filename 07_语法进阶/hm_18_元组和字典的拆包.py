def demo(*args, **kwargs):

    print(args)
    print(kwargs)


# 元组变量或者字典变量
gl_nums = (1, 2, 3)
gl_dict = {"name": "小明", "age": 18}


# 如果不在变量前加 * 号，所有变量只会存进arge
# 拆包语法简化变量的传递
demo(*gl_nums, **gl_dict)


# demo(1, 2, 3, name="小明" ,age=18)