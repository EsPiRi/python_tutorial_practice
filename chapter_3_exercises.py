# 1
from random import *
import random
import math
from math import *

for i in range(50):
    print(randint(3, 6), end="-")

# 2
print()
x = randint(1, 50)
y = randint(2, 5)
print(x, y, x ** y)

# 3
print()
x = randint(1, 10)
for i in range(x):
    print(i + 1, "- your name")

# 4
print()
x = random.uniform(1, 10)
x = (int(100 * x)) / 100
print(x)

# 5
print()
for i in range(2, 50):
    x = (int(100 * random.uniform(1, i))) / 100
    print(x, end="-")

# 6
print()
x = int(input("Enter x value: "))
y = int(input("Enter y value: "))
result = abs(x - y) / (x + y)
print(result)

# 7
print()
angle = int(input("Enter an angle between -180 and 180: "))
angle_normalized = (angle + 360) % 360
print(angle_normalized)

# 8
print()
user_input = int(input("Enter seconds to convert: "))
seconds = user_input % 60
minutes = (user_input // 60) % 60
hours = ((user_input // 60) // 60)
print("Converted time: %d Hours %d Minutes %d Seconds" % (hours, minutes, seconds))

# 9
print()
hour_now = int(input("Enter hour: "))
hours_ahead = int(input("How many hours ahead?: "))
new_hour = (hour_now + hours_ahead) % 12
print("New hour:", new_hour, "o'clock")

# 10
# a-printing the last digit of 2**input
print()
power = int(input("Enter a power: "))
number = 2 ** power
last_1_digit = number % 10
print(last_1_digit)
# b-printing the last 2 digits of 2**input
power = int(input("Enter a power: "))
number = 2 ** power
last_2_digits = number % 100
print(last_2_digits)
# c-printing the selected digits of 2**input
power = int(input("Enter a power: "))
selected_digits = int(input("Enter how many digits you wanted to see: "))
number = 2 ** power
last_selected_digits = number % (selected_digits * 10)
print(last_selected_digits)

# 11
print()
user_input = float(input("Enter a weight in kilograms: "))
kg_to_pound = 2.2 * user_input
print(kg_to_pound, "not rounded")
kg_to_pound = round(kg_to_pound / 10) * 10
print(kg_to_pound, "rounded")

# 12
print()
number = int(input("Enter a number to get its factorial: "))
print(math.factorial(number))

# 13
print()
angle = float(input("Enter an angle to see its trigonometric values: "))
print("Sine:", math.sin(angle), "\nCosine:", math.cos(angle), "\nTangent:", math.tan(angle))

# 14
print()
angle = float(input("Enter an angle to see its trigonometric values: "))
angle = math.radians(angle)
print("Sine:", math.sin(angle), "\nCosine:", math.cos(angle), "\nTangent:", math.tan(angle))

# 15
print()
for i in range(0, 360, 15):
    angle = math.radians(i)
    sin_angle = int(sin(angle) * 10000) / 10000
    cos_angle = int(cos(angle) * 10000) / 10000
    print(i, "---", sin_angle, cos_angle)

# 16 works for most of the years, some years maybe wrong
print()
Y = int(input("Enter the year you want to learn its Easter: "))
C = Y // 100
m = (15 + C - math.floor(C / 4) - math.floor((8 * C + 13) / 25)) % 30
n = (4 + C - math.floor(C / 4)) % 7
a = Y % 4
b = Y % 7
c = Y % 19
d = (19 * c + m) % 30
e = (2 * a + 4 * b + 6 * d + n) % 7
if 22 + d + e > 31:
    print("April", d + e - 9)
elif (22 + d + e) <= 31:
    print("March", 22 + d + e)

# 17
print()
year = int(input("Enter the year: "))
leap_year = False
count = 0
leap_years = list()
if year > 1600:
    print("year>1600")
    for i in range(1600, year):
        if i % 400 == 0:
            leap_year = True
            count += 1
            leap_years.append(i)
        elif i % 100 == 0:
            leap_year = False
        elif i % 4 == 0:
            leap_year = True
            count += 1
            leap_years.append(i)
else:
    print("year<1600")

print(count, "leap years in this interval are:", leap_years)

# 18
print()
price = float(input("Enter the products price: "))
given_money = float(input("Enter the given money: "))
difference = (given_money - price) * 100
if difference >= 0:
    dollars = difference // 100
    difference = difference % 100
    quarters = difference // 25
    difference = difference % 25
    dimes = difference // 10
    difference = difference % 10
    pennies = difference
    print("The change is %.0f dollars %.0f quarters %.0f dimes and %0.f pennies." % (dollars, quarters, dimes, pennies))

# 19
height = int(input("Enter the height of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
k = 0
for i in range(height):
    for j in range(width):
        print(k, end=" ")
        k = (k + 1) % 10
    print()
