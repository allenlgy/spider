def sum_2_num(num1, num2):
    """对两个数字的求和"""

    result = num1 + num2

    # 使用返回值告诉调用方计算的值
    return result


# 可以使用变量接收函数执行的结果
sum_result = sum_2_num(10, 20)

print('计算结果 %d' % sum_result)
