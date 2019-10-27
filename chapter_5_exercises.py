# 1
import math
from math import *

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
