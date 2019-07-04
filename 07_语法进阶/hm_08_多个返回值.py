def measure():
    """测量温度和湿度"""

    print("测量开始...")
    temp = 39
    wetness = 50
    print("测量结束...")

    # 元组-可以包含多个数据，因此可以让元组储存数据
    # 如果函数返回的类型是元组，可以省略小括号
    return temp, wetness

# 元组
result = measure()
print(result)

# 需要单独的处理温度和湿度 - 不方便
#print(result[0])
#print(result[1])


# 如果函数返回的类型是元组， 同时希望单独处理数据
# 可以使用多个变量一次接收函数的返回结果
# 注意: 使用多个变量接收结果时，变量的个数和元组的个数应该一致
gl_temp,gl_wetness = measure()

print(gl_temp)
print(gl_wetness)