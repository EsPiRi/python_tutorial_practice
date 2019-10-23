import math
from random import random
import random
from math import *

#15
print()
for i in range(0,360,15):
    angle=math.radians(i)
    sin_angle=int(sin(angle)*10000)/10000
    cos_angle=int(cos(angle)*10000)/10000
    print(i,"---",sin_angle,cos_angle)