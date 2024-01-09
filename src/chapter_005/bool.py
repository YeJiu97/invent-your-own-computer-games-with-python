# 布尔操作符

# 逻辑操作符
# and or not
# 优先级：not > and > or

# 逻辑操作符的短路逻辑
# and 一假则假
# or 一真则真
# not 取反

# 例子
# 1. 逻辑操作符的优先级
print(True or False and False) # 解释：True or (False and False) = True or False = True
print(True and False or False) # 解释：(True and False) or False = False or False = False
print(not True or False and False) # 解释：not True or (False and False) = False or False = False
print(not True and False or False) # 解释：(not True and False) or False = False or False = False
print(not True and False or True) # 解释：(not True and False) or True = False or True = True
print(not True or False and True) # 解释：not True or (False and True) = False or False = False
print(not True or True and False) # 解释：not True or (True and False) = False or False = False
print(not True and True or False) # 解释：(not True and True) or False = False or False = False
print(not True and True or True) # 解释：(not True and True) or True = False or True = True
print(not True or True and True) # 解释：not True or (True and True) = False or True = True
print(not True and True or True) # 解释：(not True and True) or True = False or True = True