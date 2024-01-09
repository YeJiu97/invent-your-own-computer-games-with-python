# 布尔值
# 布尔值只有True、False两种值，要么是True，要么是False， 在Python中，可以直接用True、False表示布尔值（请注意大小写），也可以通过布尔运算计算出来：
# 布尔值可以用and、or和not运算。
# and运算是与运算，只有所有都为True，and运算结果才是True：
print(True and True)
print(True and False)
print(False and False)
print(5 > 3 and 3 > 1)
# or运算是或运算，只要其中有一个为True，or运算结果就是True：
print(True or True)
print(True or False)
print(False or False)
print(5 > 3 or 1 > 3)
# not运算是非运算，它是一个单目运算符，把True变成False，False变成True：
print(not True)
print(not False)
print(not 1 > 2)
# 布尔值经常用在条件判断中，比如：
age = 20
if age >= 18:
    print('adult')
else:
    print('teenager')


# loop语句

# 1.for循环
# for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
# for循环的语法格式如下：
# for iterating_var in sequence:
#     statements(s)

# 实例
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in list:
    print(num)

# 2.while循环
# while循环的语法格式如下：
# while 判断条件(condition)：
#     执行语句(statements)……

# 实例
count = 0
while count < 9:
    print('The count is:', count)
    count = count + 1
print("Good bye!")

# 3.循环嵌套
# Python语言允许在一个循环体里面嵌入另一个循环。
# 实例
i = 2
while (i < 100):
    j = 2
    while (j <= (i / j)):
        if not (i % j): break
        j = j + 1
    if (j > i / j):
        print(i, " 是素数")
    i = i + 1
print("Good bye!")

# 4.无限循环
# 如果条件判断语句永远为true，循环将会无限的执行下去。
# 实例
var = 1
while var == 1:  # 表达式永远为true
    num = input("Enter a number  :")
    print("You entered: ", num)
# 可以使用 CTRL+C 来退出当前的无限循环。

# 5.循环使用else语句
# 在python中，while … else 在循环条件为 false 时执行 else 语句块：
# 实例
count = 0
while count < 5:
    print(count, " is  less than 5")
    count = count + 1
else:
    print(count, " is not less than 5")

# 6.简单语句组
# 类似if语句的语法，如果你的while循环体中只有一条语句，你可以将该语句与while写在同一行中， 如下所示：
# 实例
flag = 1
while (flag): print('Given flag is really true!')

# break语句
# break语句可以跳出for和while的循环体。如果你从for或while循环中终止，任何对应的循环else块将不执行。
# 实例
for letter in 'Python':  # 第一个实例
    if letter == 'h':
        break
    print('Current Letter :', letter)