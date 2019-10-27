import math
from random import random
import random
from math import *

# 14
# a
print()
win_count = 0
lose_count = 0
played_game = 10000
A = "A"
B = "B"
C = "C"
doors = ["A", "B", "C"]
# switch selected the door
for i in range(played_game):
    prize = random.choice(doors)
    selection = random.choice(doors)

    if selection == prize:
        remaining = list(set(doors) - set(prize))
        open_door = random.choice(list(set(doors) - set(random.choice(remaining))))
        alternate = random.choice(list(set(doors) - set(open_door) - set(prize)))
    else:
        open_door = random.choice(list(set(doors) - set(prize) - set(selection)))
        alternate = random.choice(list(set(doors) - set(selection) - set(open_door)))

    # print("The door I going to open is: %s" % open_door)
    second_chance = "Yes"

    if second_chance == "Yes":
        # print("The door you switched is %s" % alternate)
        if alternate == prize:
            # print("Congratulations, you win the prize")
            win_count += 1
        else:
            # print("Sorry, the prize was behind the original door %s" % prize)
            lose_count += 1

    if second_chance != "Yes":
        # print("You decided to keep your door %s" % selection)
        if selection != prize:
            #    print("Sorry, the prize was behind the alternate door %s" % prize)
            lose_count += 1
        else:
            #   print("Congratulations, you win the prize!")
            win_count += 1

print("Case 0: Switch the selected door ")
print("Win percentage: %.4f" % ((win_count / played_game) * 100))

# keep the selected door
for i in range(played_game):
    win_count = 0
    lose_count = 0
    prize = random.choice(doors)
    selection = random.choice(doors)

    if selection == prize:
        remaining = list(set(doors) - set(prize))
        open_door = random.choice(list(set(doors) - set(random.choice(remaining))))
        alternate = random.choice(list(set(doors) - set(open_door) - set(prize)))
    else:
        open_door = random.choice(list(set(doors) - set(prize) - set(selection)))
        alternate = random.choice(list(set(doors) - set(selection) - set(open_door)))

    # print("The door I going to open is: %s" % open_door)
    second_chance = "No"

    if second_chance == "Yes":
        # print("The door you switched is %s" % alternate)
        if alternate == prize:
            # print("Congratulations, you win the prize")
            win_count += 1
        else:
            # print("Sorry, the prize was behind the original door %s" % prize)
            lose_count += 1

    if second_chance != "Yes":
        #  print("You decided to keep your door %s" % selection)
        if selection != prize:
            #   print("Sorry, the prize was behind the alternate door %s" % prize)
            lose_count += 1
        else:
            #  print("Congratulations, you win the prize!")
            win_count += 1

print("Case 1: Keep the selected door")
print("Win percentage: %.4f" % ((win_count / played_game) * 100))

# b
# playing game with 4 doors 1 prize
win_count = 0
lose_count = 0
played_game = 10000
A = "A"
B = "B"
C = "C"
D = "D"
doors = ["A", "B", "C", "D"]
for i in range(played_game):
    prize = random.choice(doors)
    selection = random.choice(doors)

    if selection == prize:
        remaining = list(set(doors) - set(prize))
        open_door = random.choice(list(set(doors) - set(random.choice(remaining))))
        alternate = random.choice(list(set(doors) - set(open_door) - set(prize)))
    else:
        open_door = random.choice(list(set(doors) - set(prize) - set(selection)))
        alternate = random.choice(list(set(doors) - set(selection) - set(open_door)))

    # print("The door I going to open is: %s" % open_door)
    second_chance = "Yes"

    if second_chance == "Yes":
        # print("The door you switched is %s" % alternate)
        if alternate == prize:
            # print("Congratulations, you win the prize")
            win_count += 1
        else:
            # print("Sorry, the prize was behind the original door %s" % prize)
            lose_count += 1

    if second_chance != "Yes":
        # print("You decided to keep your door %s" % selection)
        if selection != prize:
            #    print("Sorry, the prize was behind the alternate door %s" % prize)
            lose_count += 1
        else:
            #   print("Congratulations, you win the prize!")
            win_count += 1

print("Case 0: Switch the selected door with 4 doors ")
print("Win percentage: %.4f" % ((win_count / played_game) * 100))

# keep the selected door
for i in range(played_game):
    win_count = 0
    lose_count = 0
    prize = random.choice(doors)
    selection = random.choice(doors)

    if selection == prize:
        remaining = list(set(doors) - set(prize))
        open_door = random.choice(list(set(doors) - set(random.choice(remaining))))
        alternate = random.choice(list(set(doors) - set(open_door) - set(prize)))
    else:
        open_door = random.choice(list(set(doors) - set(prize) - set(selection)))
        alternate = random.choice(list(set(doors) - set(selection) - set(open_door)))

    # print("The door I going to open is: %s" % open_door)
    second_chance = "No"

    if second_chance == "Yes":
        # print("The door you switched is %s" % alternate)
        if alternate == prize:
            # print("Congratulations, you win the prize")
            win_count += 1
        else:
            # print("Sorry, the prize was behind the original door %s" % prize)
            lose_count += 1

    if second_chance != "Yes":
        #  print("You decided to keep your door %s" % selection)
        if selection != prize:
            #   print("Sorry, the prize was behind the alternate door %s" % prize)
            lose_count += 1
        else:
            #  print("Congratulations, you win the prize!")
            win_count += 1

print("Case 1: Keep the selected door with 4 doors")
print("Win percentage: %.4f" % ((win_count / played_game) * 100))
