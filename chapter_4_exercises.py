# 1
import random

cm = int(input("Enter a length in centimeters: "))
if cm < 0:
    print("Length cannot be negative!")
else:
    print("Centimeters: %d, Inches: %.2f" % (cm, cm / 2.54))

# 2
print()
temperature = float(input("Enter a temperature: "))
selection = int(input("Which unit you want to use?\n1. Celsius\n2. Fahrenheit\n"))
if selection == 1:
    print("The temperature in Fahrenheit is", (9 / 5) * temperature + 32)
if selection == 2:
    print("The temperature in Celsius is", (5 / 9) * (temperature - 32))

# 3
print()
temperature = float(input("Enter a temperature in Celsius: "))
if temperature < -273.15:
    print("This temperature is below absolute zero!")
elif temperature == -273.15:
    print("This temperature is absolute zero!")
elif -273.15 < temperature < 0:
    print("The temperature is below freezing")
elif temperature == 0:
    print("The temperature is at the freezing point")
elif 0 < temperature < 100:
    print("The temperature is in the normal range")
elif temperature == 100:
    print("The temperature is at the boiling point")
elif temperature > 100:
    print("The temperature is above the boiling point")

# 4
print()
credit_taken = int(input("Enter how many credits you have taken: "))
if 0 < credit_taken <= 23:
    print("You are a freshman")
elif 23 < credit_taken <= 53:
    print("You are a sophomore")
elif 53 < credit_taken <= 83:
    print("You are a junior")
elif credit_taken > 83:
    print("You are a senior")

# 5
print()
random_number = random.randint(1, 10)
# print(random_number) this line is for trying the code whether correct answer works or not.
guess = int(input("Enter your guess: "))
if guess == random_number:
    print("You got the point!")
else:
    print("Your guess is wrong.")

# 6
print()
price = 0
item_count = int(input("Enter the number of piece you want to buy: "))
if item_count < 10:
    price = item_count * 12
elif 10 <= item_count < 100:
    price = item_count * 10
elif item_count >= 100:
    price = item_count * 7

print("Price: $", price)

# 7
print()
number1 = float(input("Enter number 1: "))
number2 = float(input("Enter number 2: "))
if abs(number1 - number2) <= 0.001:
    print("Close")
else:
    print("Not close")

# 8
print()
year = int(input("Enter the year: "))
leap_year = False
if year >= 1600:
    if year % 400 == 0:
        leap_year = True
    elif year % 100 == 0:
        leap_year = False
    elif year % 4 == 0:
        leap_year = True
else:
    print("year<1600")

if leap_year:
    print("The year you entered is a leap year.")
else:
    print("The year you entered is not a leap year.")

# 9
print()
number = int(input("Enter number to see its divisors: "))
divisors = list()
for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(i)

print("The divisors of entered number are:", divisors)

# 10
print()
for i in range(1, 11):
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    answer = int(input("Question %d: %d x %d = " % (i, number1, number2)))
    if answer == (number1 * number2):
        print("Right!")
    else:
        print("Wrong. The answer is %d" % (number1 * number2))
