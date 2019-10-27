import math
import re
from random import random
import random
from math import *

#4
word=input("Enter a word: ")
contains_vowel=False
for letter in ["a","e","i","o","u","A","E","I","O","U"]:
    if letter in word:
        contains_vowel=True

if contains_vowel:
    print("This word contains at least one vowel.")
else:
    print("This word doesn't contain any vowel")