# 1. 输入苹果的单价
price = float(input("输入苹果的单价："))
# 2. 输入苹果的重量
weight = float(input("输入苹果的重量："))
# 3. 计算支付的总金额
# 两个字符串变量之间是不能互相乘
money = price * weight
print(money)