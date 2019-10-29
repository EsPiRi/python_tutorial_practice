import math
import re
from random import random
import random
from math import *
from collections import *

# 22
# a
word = list(input("Enter a word to encrypt: "))
encrypted_word = ""
decrypted_word = list(range(len(word)))
for i in range(0, len(word), 2):
    encrypted_word += "".join(word[i])

for i in range(1, len(word), 2):
    encrypted_word += "".join(word[i])

for i in encrypted_word:







print(encrypted_word)
print(decrypted_word)
