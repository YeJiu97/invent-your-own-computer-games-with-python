# guess number game
# rule
# 1. guess a number between 1-100
# 2. if guess right, print "you win!"
# 3. if guess wrong, print "guess bigger" or "guess smaller"
# 4. you have 5 chances to guess
# 5. if you lose, print "you lose!"

import random
secret_number = random.randint(1, 100)
guess_count = 0
guess_limit = 5
print("guess number game")
print("rule")
print("1. guess a number between 1-100")
print("2. if guess right, print \"you win!\"")
print("3. if guess wrong, print \"guess bigger\" or \"guess smaller\"")
print("4. you have 5 chances to guess")
print("5. if you lose, print \"you lose!\"")
print("let's start!")
while guess_count < guess_limit:
    guess = int(input("enter a number: "))
    guess_count += 1
    if guess == secret_number:
        print("you win!")
        break
    elif guess > secret_number:
        print("guess smaller")
    else:
        print("guess bigger")
else:
    print(secret_number)
    print("you lose!")
print("game over!")