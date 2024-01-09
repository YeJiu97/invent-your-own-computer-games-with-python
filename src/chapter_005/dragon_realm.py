# dragon realm game
# 游戏规则
# 玩家在两个洞穴中选择一个进入
# 一个山洞里面有一条友好的龙，会把宝藏给你
# 另一个山洞里面有一条凶猛的龙，会吃掉你

import random
import time # import time因为要用到time.sleep()函数

def displayIntro():
    print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.''')
    print() # print()函数用于换行

def chooseCave():
    cave = ''
    # 考虑到用户可能输入错误，所以用while循环
    while cave != '1' and cave != '2': # while循环，只要cave不等于1或者2，就一直循环
        print('Which cave will you go into? (1 or 2)')
        cave = input()
    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2) # time.sleep()函数用于暂停程序，括号里面的数字代表暂停的秒数
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    # 用random.randint()函数随机生成一个1或者2
    friendlyCave = random.randint(1, 2)

    # 如果用户输入的洞穴号等于随机生成的洞穴号，就打印You win!
    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    # 如果用户输入的洞穴号不等于随机生成的洞穴号，就打印Gobbles you down in one bite!
    else:
        print('Gobbles you down in one bite!')

playAgain = 'yes'
# 考虑到用户可能输入错误，所以用while循环
while playAgain == 'yes' or playAgain == 'y': # while循环，只要playAgain等于yes或者y，就一直循环
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    # 用input()函数让用户输入yes或者no
    print('Do you want to play again? (yes or no)')
    playAgain = input()
    # 如果用户输入的是yes或者y，就继续循环
    # 如果用户输入的是no或者n，就退出循环
    # 如果用户输入的既不是yes或者y，也不是no或者n，就继续循环
    # 用lower()函数把用户输入的字符串转换成小写
    if playAgain.lower() == 'no' or playAgain.lower() == 'n':
        break