i = 0

while i < 10:

    # continue 某一条件满足时，不执行后面的代码
    # 注意，在循环中，如果使用 continue 必须确认循环的次数是否修改
    # 如果没改，很可能陷入死循环
    if i == 3:
        i += 1

        continue
    print(i)

    i += 1