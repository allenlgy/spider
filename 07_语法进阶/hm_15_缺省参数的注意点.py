# 缺省值一定要放在函数末尾
def print_info(name, title="", gender=True):
    """

    :param title: 职位
    :param name: 班上同学的姓名
    :param gender:  True 男生 False 女生
    :return:
    """
    gender_text = "男生"

    if not gender:
        gender_text = "女生"

    print("[%s]%s 是 %s"%(title, name, gender_text))


# 假设班上的同学男生居多
# 应该使用最常用的值作为缺省值
print_info("小明")
print_info("老王")
print_info("xiaomei", "经理", gender=False)
