import math
from random import random
import random
from math import *

#2
print()
temperature=float(input("Enter a temperature: "))
selection=int(input("Which unit you want to use?\n1. Celsius\n2. Fahrenheit\n"))
if selection==1:
    print("The temperature in Fahrenheit is",(9/5)*temperature+32)
if selection==2:
    print("The temperature in Celsius is", (5/9)*(temperature-32))
