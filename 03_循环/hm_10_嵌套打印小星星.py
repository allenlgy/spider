# 输出五行星号
# 1.完成 5 行简单输出
# 2.分析每行内部的星号如何处理

row = 1

while row <= 5:

    # 每一行打印的星星就是当前的行数
    # 增加一个小循环
    # 1.定义一个计数器变量
    col = 1

    # 2.开始循环
    while col <= row:

        # print('%d' % col)
        print('*',end='')
        col += 1
    # print('第 %d 行' % row)
    # 下面的 print 是为了增加换行，不然不会换
    print('')
    row += 1