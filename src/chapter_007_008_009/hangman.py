# hangman游戏规则
# 首先有一个单词列表
# 接着从这个单词列表中随机抽取一个单词，要求玩家进行猜测
# 玩家一共有6次机会
# 如果玩家猜对了单词，这将这个单词的这个字符显示出来，例如：_a_a_a为banana单词才对a的时候的显示
# 如果玩家操作了单词，则消耗一次机会，但是采取的字符会被显示，例如：wrong character: ['c', 'd']
# 如果玩家在6次以内猜出了完整的单词，则玩家获得胜利
# 如果玩家在6次以内猜没有猜出完整的单词，则玩家失败
# 游戏需要进行循环，直到玩家选择推出游戏
# 单词只由字符串组成，并且都是小写，所以需要考虑玩家输入的大小写问题，并且考虑玩家输入不合法的字符的问题

# 导入必备的模块
import random
import os

# Hangman的图形
# 这里所有字母都是大写字母，这表示这是一个常量
# Python的常量不是从技术上实现的，而是表示的时候这么表示的
HANG_MAN_PICS = ['''
    +---+
        |
        |
        |
         ===''', '''
    +---+
    O   |
        |
        |
         ===''', '''
    +---+
    O   |
    |   |
        |
         ===''', '''
    +---+
    O   |
    /|   |
          |
            ===''', '''
    +---+
    O   |
    /|\  |
          |
            ===''', '''
    +---+
    O   |
    /|\  |
    /     |
            ===''', '''
    +---+
    O   |
    /|\  |
    / \  |
            ===''']

# 生成一个单词列表
fruits = ["apple", "banana", "orange", "grape", "strawberry", "blueberry", "watermelon", "pineapple",
"mango", "peach", "pear", "cherry", "plum", "kiwi", "lemon", "lime", "coconut", "papaya", "apricot", "avocado"]

# 生成一个函数，用来随机抽取一个单词
def get_a_word(words):
	"""这个函数会从单词列表中随机抽取一个单词"""
	word = random.choice(fruits)
	return word

'''
另外一种写法

def get_a_word(words):
	"""使用随机数来完成"""
	random_number = random.randint(0, len(fruits) - 1)
	return fruites[random_number]
'''

# 要求用户输入开决定开始游戏还是结束游戏
def start_end():
	# 首先要求用户输入数字
	player_choice = int(input("""
		1. 开始游戏
		2. 推出游戏"""))
	while player_choice.isdigit():
		player_choice = int(input("""
		1. 开始游戏
		2. 推出游戏"""))

	return player_choice

# 要求用户输入

def run_game():
	"""这个程序用来运行"""
	if start_end() == 1:
		# 开始游戏
	else:
		# 结束游戏 break
