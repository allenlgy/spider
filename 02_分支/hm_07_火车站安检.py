# 定义布尔变量 has_ticket 表示是否有车票
has_ticket = True

# 定义整型变量 knife_length 表示刀的长度
knife_length = 10

# 说先检查是否有车票，如果有才进行安检
if has_ticket:
    print('车票通过')

    # 安检时 需要检查刀的长度，判断是否超过 20 厘米
    # 如果超过，不允许上车
    if knife_length >20:
        print('刀太长。您携带的刀有 %d 米长' %knife_length)

    # 如果不超过，安检通过
    else:
        print('安检通过')

# 如果没有车票，不允许进门
else:
    print('没票，不允许上车')
