import math
from random import random
import random
from math import *

#8
# 17
print()
year = int(input("Enter the year: "))
leap_year = False
count = 0
leap_years = list()
if year >= 1600:
    if year % 400 == 0:
        leap_year = True
        count += 1
    elif year % 100 == 0:
        leap_year = False
    elif year % 4 == 0:
        leap_year = True
        count += 1
else:
    print("year<1600")

if leap_year:
    print("The year you entered is a leap year.")
else:
    print("The year you entered is not a leap year.")