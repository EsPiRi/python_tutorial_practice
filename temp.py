import math
import re
from random import random
import random
from math import *
from collections import *

# 19
print()
number = list(input("Enter a large integer (e.g 1 million)"))
new_number=""
if len(number) % 3 == 0:
    for i in range(len(number)):
        if (i%3==2)&(i<len(number)-1):
            new_number+=number[i]+","
        else:
            new_number+=number[i]

elif len(number)%3==1:
    new_number+=number[0]+","
    for i in range(1,len(number)):
        if (i%3==0)&(i<len(number)-1):
            new_number+=number[i]+","
        else:
            new_number+=number[i]
elif len(number)%3==2:
    new_number+=number[0]+number[1]+","
    for i in range(2,len(number)):
        if (i%3==1)&(i<len(number)-1):
            new_number+=number[i]+","
        else:
            new_number+=number[i]

print(new_number)

