import random

uppercase_letters ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits ="0123456789"
symbols = ",.:;'@#$&*()"


upper, lower, nums, symb = True, True,True,True

all =""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if symb:
    all += symbols
    
length = 10
amount = 8

for x in range (amount):
    password = "".join(random.sample(all, length))
print(password)