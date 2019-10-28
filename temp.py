import math
import re
from random import random
import random
from math import *

#14
print()
name=list(input("Enter your name in lowercase: ").split())
print(name)
for i in range(len(name)):
    temp=list(name[i])
    temp[0]=temp[0].upper()
    name[i]="".join(temp)

name=" ".join(name)
print(name)

