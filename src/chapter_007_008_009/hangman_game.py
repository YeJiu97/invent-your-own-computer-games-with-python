import random
import os

# 首先是一个单词列表，作为常量用来存储单词
WORDS = [ 'apple', 'banana', 'orange', 'coconut', 'strawberry', 'lime', 'grapefruit', 
         'lemon', 'kumquat', 'blueberry', 'melon', 'mango', 'papaya', 'peach', 'persimmon', 
         'raspberry', 'tangerine', 'watermelon', 'durian', 'starfruit' ]

# 一共有7次猜错的机会
MAX_WRONG = 7

# 接着是hangman的图像，用来显示游戏进度
HANGMAN_PICS = [ '''
        +---+
        |   |
        |
        |
        |
        |
        =========''', '''
        +---+
        |   |
        |   O
        |
        |
        |
        =========''', '''
        +---+
        |   |
        |   O
        |   |
        |
        |
        =========''', '''
        +---+
        |   |
        |   O
        |  /|
        |
        |
        =========''', '''
        +---+
        |   |
        |   O
        |  /|\\
        |
        |
        =========''', '''
        +---+
        |   |
        |   O
        |  /|\\
        |  /
        |
        =========''', '''
        +---+
        |   |
        |   O
        |  /|\\
        |  / \\
        |
        =========''']

# 打印游戏的欢迎信息
def welcome():
    print('''
    欢迎来到猜单词游戏！
    猜对单词，你就能活下来！
    猜错单词，你就会被绞死！
    你一共有7次机会！
    祝你好运！
    ''')

# 要求玩家选择开始游戏或者退出游戏
def start_or_quit():
    print('''
    请选择：
    1. 开始游戏
    2. 退出游戏
    ''')
    choice = input('请选择：')
    while choice != '1' and choice != '2':
        choice = input('请选择：')
    return choice

# 从单词列表中随机选择一个单词
def get_word():
    word = random.choice(WORDS)
    return word

# 打印游戏的状态，包括hangman图像和已经猜过的字母
def display_board(missed_letters, correct_letters, secret_word):
    print(HANGMAN_PICS[len(missed_letters)])
    print()

    print("猜错的字符：", end = "")
    for letter in missed_letters:
        print(letter, end = ' ')
    print()

    blanks = '_' * len(secret_word)  # 用来存储单词的空白字符串

    # 将已经猜对的字母填入空白字符串中
    for i in range(len(secret_word)):  # 遍历单词的每一个字母
        if secret_word[i] in correct_letters:  # 如果字母在已经猜对的字母列表中
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]  # 字符串是不可变类型，所以这里要重新赋值
    
    for letter in blanks:  # 打印空白字符串
        print(letter, end = ' ')  # end = ' ' 表示打印完毕后不换行
    print()  # 换行

# 获取玩家猜的字母
def get_guess(already_guessed):
    guess = input('请猜一个字母：')
    # 如果输入的不是一个字母，或者输入的是已经猜过的字母，就要求玩家重新输入
    while guess == '' or len(guess) != 1 or guess not in 'abcdefghijklmnopqrstuvwxyz':
        guess = input('请猜一个字母：')
    guess = guess.lower()  # 将字母转换为小写
    # 如果玩家猜过这个字母，就要求玩家重新输入
    while guess in already_guessed:
        guess = input('你已经猜过这个字母了，请猜一个新的字母：')
        guess = guess.lower()
    return guess

# 游戏运行程序
def run_game():
    """游戏运行程序"""
    welcome()  # 打印游戏的欢迎信息
    choice = start_or_quit()  # 要求玩家选择开始游戏或者退出游戏

    # 开始进行游戏循环
    while choice == '1':
        