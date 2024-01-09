# 字符串是文本值，可以将字符串存储到变量中，或者直接作为参数传递给函数。
hello = 'Hello, world!'
print(hello)

# 字符串可以使用单引号或双引号括起来，但不能混用。
# 以下代码会导致报错
# hello = 'Hello World"

# 字符串中的引号
# 如果字符串中包含单引号或双引号，可以使用转义字符\来标识
comment = "he said \"I am a student\""
print(comment)

# 或者可以单引号作为整个字符串的标识
comment = 'he said "I am a student"'
print(comment)

# 字符串可以通过+号进行拼接
first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + ' ' + last_name
print(full_name)

# 程序可以使用input()函数获取用户输入
# input()函数接受一个参数，即要向用户显示的提示或说明
# input()函数返回的值都是字符串
name = input('Please enter your name: ')

# 如果要将输入的字符串转换为数值，可以使用int()函数
# int()函数将数字字符串转换为数值表示
age = input('How old are you? ')
age = int(age)
print(age >= 18)