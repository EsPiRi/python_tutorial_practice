# 1
import math
from math import *
from random import *

count = 0
for i in range(1, 101):
    if i ** 2 % 10 == 1:
        print(i)
        count += 1

print(count)

# 2
print()
count_4 = 0
count_9 = 0
for i in range(1, 101):
    if i ** 2 % 10 == 4:
        print(i, "sq4")
        count_4 += 1
    elif i ** 2 % 10 == 9:
        print(i, "sq9")
        count_9 += 1

print(count_4, count_9)

# 3
print()
n = int(input("Enter n value: "))
total = 1
for i in range(1, n):
    total += 1 / n
print(total - math.log(n, e))

# 4
print()
total = 0
for i in range(1, 2001):
    if i % 2 == 1:
        total += i
    else:
        total -= i

print(total)

# 5
print()
number = int(input("Enter a number to see its sum of divisors: "))
total = 0
for i in range(1, number // 2 + 1):
    if number % i == 0:
        print(i, end=" ")
        total += i

print(number)
print(total, total + number)

# 6
print()
for i in range(1, 10000):
    sum_of_divisors = 0
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            sum_of_divisors += j

    if sum_of_divisors == i:
        print(i)

# 7
print()


def is_square_free(n):
    if n % 2 == 0:
        n = n / 2

    if n % 2 == 0:
        return False

    for i in range(3, int(sqrt(n) + 1)):

        if n % i == 0:
            n = n / i

        if n % i == 0:
            return False
    return True


number = int(input("Enter a number: "))

if is_square_free(number):
    print("Yes")
else:
    print("No")

# 8
print()
x = 1
y = 2
z = 3
print("Before swapping: x=%d y=%d z=%d" % (x, y, z))
x, y, z = y, z, x
print("After swapping: x=%d y=%d z=%d" % (x, y, z))

# 9
print()
count_square = 0
count_cubes = 0
count_fifth = 0

for i in range(1, 1000):
    for j in range(1, i // 2 + 1):
        if j ** 2 == i:
            print(j, i, "square")
            count_square += 1
        elif j ** 3 == i:
            print(j, i, "cube")
            count_cubes += 1
        elif j ** 5 == i:
            print(j, i, "fifth")
            count_fifth += 1

print(count_square, count_cubes, count_fifth)

# 10
print()
scores = list()
greater_than_100 = False
for i in range(10):
    a = int(input("Enter a score: "))
    scores.append(a)
    if a > 100:
        greater_than_100 = True
scores.sort()
# d
if greater_than_100:
    print("1 or more scores are greater than 100!")
else:
    # a
    print("Highest score:", scores[len(scores) - 1])
    print("Lowest score:", scores[0])
    # b
    print("Average score:", sum(scores) / len(scores))
    # c
    print("Second highest score:", scores[scores.index(max(scores)) - 1])
    # e
    scores.reverse()
    scores.pop()
    scores.pop()
    scores.reverse()
    print("Removed 2 lowest scores, new average is:", sum(scores) / len(scores))

# 11
print()
n = int(input("Enter a number to calculate its factorial: "))
prod = 1
for i in range(n, 0, -1):
    prod *= i

print(prod)

#12
print()
score=0
for i in range(5):
    rand_number = random.randint(1, 10)
    guess=int(input("Guess the number between 1 and 10: "))
    if guess==rand_number:
        score+=10
        print("Correct!")
    else:
        score-=1
        print("The number was",rand_number)

print("Score is:",score)

# 13
print()
correct_count = 0
wrong_count = 0
for i in range(1, 11):
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    answer = int(input("Question %d: %d x %d = " % (i, number1, number2)))
    if answer == (number1 * number2):
        print("Right!")
        correct_count += 1
    else:
        print("Wrong. The answer is %d" % (number1 * number2))
        wrong_count += 1

print("Correct answers:",correct_count)
print("Wrong answers:",wrong_count)

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
