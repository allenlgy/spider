# 导入 random 包
import random

# 从控制台输入要出的拳 1.石头 2.剪刀 3.布
player = int(input('请选择要出的拳1石头 2剪刀 3布：'))
# 电脑随机出拳——先假定电脑只会出石头，完成整体代码
computer =random.randint(1,3)

print('玩家选择的拳头是 %d,电脑出的拳是 %d' %(player,computer))

# if(()
#   or ()
#   or ())如果代码长难读可以这样
# 比较胜负
if ((player == 1 and computer ==2)
        or(player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print('玩家胜利')
elif player == computer:
    print('平局')
# 其他情况就是电脑获胜
else:
    print('电脑获胜')