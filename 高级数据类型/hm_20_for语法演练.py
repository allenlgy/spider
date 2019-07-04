for num in [1,2,3]:

    print(num)
    if num == 3:
        break

    # 如果循环不正常结束， else 不会被触发
else:
    print('over')