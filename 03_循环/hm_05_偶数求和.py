# 计算 0~100 的偶数和
i = 0
s=0

while i <= 100:
    # 判断 i 是否是偶数
    # i % 2 == 0
    if i % 2 ==0:
        s += i

    print(i)

    i += 1
print('偶数和为 %d' %s)