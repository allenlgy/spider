# 记录所有名片
card_list = []

def show_menu():

    '''显示菜单'''
    print("*" *50)
    print("欢迎使用【名片管理系统】V1.0")
    print("")
    print("1. 新增记录")
    print("2. 显示全部")
    print("3. 搜索记录")
    print("")
    print("0. 退出系统")
    print("*" *50)



def new_card():

    '''新增名片'''
    print('新增名片')

    # 1. 提示用户输入名片的详细信息
    name = input("请输入姓名：")
    phone = input("请输入电话：")
    QQ = input("请输入QQ号码：")
    email = input("请输入电子邮箱：")

    # 2. 使用用户输入的信息建立一个名片字典

    card_dict = {"name": name,
                 "phone": phone,
                 "QQ": QQ,
                 "email": email}

    # 3.将名片字典添加到列表中
    card_list.append(card_dict)

    print(card_list)

    # 4. 提示用户添加成功

    print("添加 %s 的名片成功" %name)


def show_all():

    """显示所有名片"""

    # 添加一个条件，查看列表有没有数据
    if len(card_list) == 0:
        print("列表还没有数据，请按【1】输入数据.")

        # return 返回函数的值
        # 下方的代码不会执行
        # 如果 return 后面没有任何内容，表示会返回刀函数的位置
        # 并且不返回任何结果
        return

    print('-' *50)
    print('显示所有名片')

    # 打印表头
    for name in ["name", "phone" ,"QQ" ,"email"]:
        print(name,end="\t\t")

    print("")

    # 打印分割线

    print("=" *50)


    # 遍历循环列表输出列表变量
    for card_dict in card_list:
        print('%s\t\t%s\t\t%s\t\t%s' % (card_dict["name"],
                                     card_dict["phone"],
                                     card_dict["QQ"],
                                     card_dict["email"]))



def search_card():

    """搜索名片"""

    print("-"*50)
    print("搜索成绩")

    # 1. 提示用户输入要搜索的名字

    find_name = input("请输入要搜索的名片：")

    # 2. 遍历名片列表，查询数据，如果没有

    for card_dict in card_list:

        if card_dict["name"] == find_name:

            print("姓名\t\t电话\t\tQQ\t\t邮箱\t\t")
            print("=" *50)
            print('%s\t\t%s\t\t%s\t\t%s' % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["QQ"],
                                            card_dict["email"]))
            # 针对找到的名片记录执行修改和删除的操作
            deal_card(card_dict)  # 搜索到的字典参数，使代码阅读更方便

            break

    else:
        print("没有找到%s" % find_name)


def deal_card(find_dict):
    """
    处理查找的名片
    :param find_dict: 查找的名片
    """
    #  find_dict 这个参数是上面找到的字典
    # 所以可以直接修改删除


    print(find_dict)

    action_str = input("请选择要执行的操作 "
                       "【1】.修改 【2】.删除 【0】.返回")

    if action_str == "1":

        find_dict["name"] = input_card_info(find_dict["name"], "修改姓名【空行不改】：")
        find_dict["phone"] = input_card_info(find_dict["phone"], "修改电话【空行不改】：")
        find_dict["QQ"] = input_card_info(find_dict["QQ"], "修改QQ【空行不改】：")
        find_dict["email"] = input_card_info(find_dict["email"] ,"修改邮箱【空行不改】：")

        print('修改名片成功！')

    elif action_str == "2":

        card_list.remove(find_dict)

        print('删除名片成功！')


def input_card_info(dict_value, tip_message):
    """
    输入名片信息
    :param dict_value: 字典原有的值
    :param tip_message:  新修改的值
    :return:  如果输入的值大于0，就等于修改的值否则等于原值
    """
    # 1.提示用户输入内容
    result_str = input(tip_message)

    # 2. 针对用户输入进行判断
    if len(result_str) > 0:
        return result_str

    # 3. 如果用户没有输入内容，返回值
    else:
        return dict_value
