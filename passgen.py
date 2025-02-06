import random
symbols="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
print(symbols)
passs=""
for i in range(int(input("enter length:\n  "))):
    passs+=random.choice(symbols)
print(passs)
