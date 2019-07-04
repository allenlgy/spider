# 打印 9 行小星星
# 最外层为行，里面是列的循环
row = 1

while row <= 9:

    col = 1

    while col <= row:

        # print('*',end="")
        print('%dx%d=%d'%(col,row,col*row),end="\t")

        col += 1

    #print('%d' %row)
    print('')

    row += 1