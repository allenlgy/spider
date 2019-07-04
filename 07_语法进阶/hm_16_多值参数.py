def demo(num, *args, **kw):

    print(num)
    print(args)
    print(kw)


# demo(1)
demo(1, 2, 3, 4, 5, name="小明", age=18)