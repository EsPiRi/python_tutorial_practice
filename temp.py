import math
from random import random
import random
from math import *

# 18
height = int(input("Enter the height of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
k = 0
for i in range(height):
    for j in range(width):
        print(k, end=" ")
        k =(k+1)%10
    print()
