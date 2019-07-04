# 定义字符串变量 name
name = "小"
print("我的名字叫 %s,请多多关照" % name)

# 定义整数变量 student_no,%06d是如果数字没有六位，则前面自动补零
student_no = 200000
print("学生学号为 %06d" %student_no)

# 定义小数%f，float类型,%.2f显示两位小数,可以任意改
price = 8.5
weight = 7.5
money = price * weight
print("苹果单价 %.2f,购买了 %.3f 斤， 一共用了 %.4f 元" %(price,weight,money))

# 定义个小数，输出百分号
sale = 0.25
print("数据比例是 %.2f%%" % (sale * 100) )