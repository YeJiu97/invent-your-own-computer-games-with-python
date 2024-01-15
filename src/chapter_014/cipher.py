# 首先是所有的大小写字母
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
# 然后是key的大小
MAX_KEY_SIZE = len(SYMBOLS)

# 加密还是解密
def geMode():
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        mode = input().lower()
        if mode in ['encrypt','e','decrypt','d']:
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

# 获得信息
def getMessage():
    print('Enter your message:')
    return input()

# 获得key
def getKey():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

# 加密或者解密
def getTranslatedMessage(mode,message,key):
    # 如果是解密，那么key就是负数
    if mode[0] == 'd':
        key = -key
    
    # 用来存储加密或者解密后的信息
    translated = ''

    # 对每一个字符进行加密或者解密
    for symbol in message:
        # 如果是字母，那么就加密或者解密
        symbolIndex = SYMBOLS.find(symbol)  # find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内
        if symbolIndex == -1:  # -1表示没有找到
            translated += symbol  # 不是字母，就直接加上去
        else:
            symbolIndex += key
            if symbolIndex >= len(SYMBOLS):
                symbolIndex -=len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)

            translated += SYMBOLS[symbolIndex]
    return translated

# 调用函数
mode = geMode()
message = getMessage()
key = getKey()
print('Your translated text is:')
print(getTranslatedMessage(mode,message,key))