import math
import re
from random import random
import random
from math import *
from collections import *

# 23
# general solution
word = input("Enter string to encrypt: ")
ladder_length = int(input("Enter rail length: "))
encrypted_word = ""
decrypted_word = list(range(len(word)))
for j in range(ladder_length):
    for i in range(j, len(word), ladder_length):
        encrypted_word += "".join(word[i])

for i in range(len(encrypted_word)):
    decrypted_word[i] = encrypted_word[(i * (ladder_length + 2)) % len(encrypted_word)]

print(encrypted_word)
print("".join(decrypted_word))
