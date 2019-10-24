import math
from random import random
import random
from math import *

# 10
print()
for i in range(1, 11):
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    answer = int(input("Question %d: %d x %d = " % (i, number1, number2)))
    if answer == (number1 * number2):
        print("Right!")
    else:
        print("Wrong. The answer is %d" % (number1 * number2))