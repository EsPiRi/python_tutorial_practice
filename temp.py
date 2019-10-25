import math
from random import random
import random
from math import *

# 13
print("Welcome to the Rock-Paper-Scissors Game!")
player_score=0
cpu_score=0
for i in range(5):
    print("Select your move: Rock(1) Paper(2) Scissors(3)")
    select = int(input())
    cpu_selection=random.randint(1,3)
    if select==cpu_selection:
        print("Draw",cpu_selection)
    elif select-cpu_selection==-1|select-cpu_selection==2:
        print("Cpu got the point",cpu_selection)
        cpu_score+=1
    else:
        print("Player got the point",cpu_selection)
        player_score+=1

if player_score>cpu_score:
    print("Player wins the game",player_score,cpu_score)
elif player_score<cpu_score:
    print("Cpu wins the game",player_score,cpu_score)
else:
    print("Tie game",player_score,cpu_score)