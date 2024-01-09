import random

# 介绍random模块
# random模块用于生成随机数
# random.random()用于生成一个0到1的随机符点数: 0 <= n < 1.0
random_num = random.random()
print(random_num)

# random.uniform(a, b)用于生成一个指定范围内的随机符点数: a <= n <= b
random_num = random.uniform(1, 10)
print(random_num)

# random.randint(a, b)用于生成一个指定范围内的整数: a <= n <= b
random_num = random.randint(1, 10)
print(random_num)

# random.randrange(start, stop[, step])用于生成一个指定范围内的整数: start <= n < stop
random_num = random.randrange(1, 10)
print(random_num)

# random.choice(sequence)用于从序列中获取一个随机元素
random_num = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(random_num)

# random.shuffle(x[, random])用于将一个列表中的元素打乱
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(list)
print(list)

# random.sample(sequence, k)用于从指定序列中随机获取指定长度的片段
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
slice = random.sample(list, 5)
print(slice)

# random.seed([x])用于改变随机数生成器的种子seed
random.seed(10)
print(random.random())