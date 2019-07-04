# 在默认情况下， print 函数会在末尾自动加上换行
for i in range(3):
    print(i)


# 要想不要换行，可以加上
for i in range(3):
    print(i,end='')