# python函数
# 1.函数的定义
# 函数是一段可以重复使用的代码块，可以接受参数，可以返回值。
# 函数的定义格式如下：
# def 函数名(参数1, 参数2, ...):
#     函数体
#     return 返回值
# 2.函数的调用
# 函数的调用格式如下：
# 函数名(参数1, 参数2, ...)
# 3.函数的参数
# 函数的参数是函数的输入，函数的参数可以有多个，也可以没有。
# 4.函数的返回值
# 函数的返回值是函数的输出，函数的返回值可以有多个，也可以没有。

# 函数例子
# 1.函数的定义
def add(x, y):
    z = x + y
    return z

# 2.函数的调用
print(add(1, 2))

# 3.函数的参数
def add(x, y):
    z = x + y
    return z

print(add(1, 2))

# 4.函数的返回值
def add(x, y):
    z = x + y
    return z

print(add(1, 2))

# 不确定参数个数的函数
# 1.不确定参数个数的函数的定义
# 不确定参数个数的函数的定义格式如下：
# def 函数名(*参数):
#     函数体
#     return 返回值
# 2.不确定参数个数的函数的调用
# 不确定参数个数的函数的调用格式如下：
# 函数名(参数1, 参数2, ...)
# 3.不确定参数个数的函数的参数
# 不确定参数个数的函数的参数是函数的输入，不确定参数个数的函数的参数可以有多个，也可以没有。
# 4.不确定参数个数的函数的返回值
# 不确定参数个数的函数的返回值是函数的输出，不确定参数个数的函数的返回值可以有多个，也可以没有。

# 不确定参数个数的函数例子
# 1.不确定参数个数的函数的定义
def add(*args):
    z = 0
    for i in args:
        z += i
    return z

# 2.不确定参数个数的函数的调用
print(add(1, 2, 3, 4, 5))

# 3.不确定参数个数的函数的参数
def add(*args):
    z = 0
    for i in args:
        z += i
    return z

print(add(1, 2, 3, 4, 5))

# 4.不确定参数个数的函数的返回值
def add(*args):
    z = 0
    for i in args:
        z += i
    return z