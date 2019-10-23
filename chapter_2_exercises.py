# 1 and 3
name = input("Enter your name: ")

for i in range(100):  # solution 1 and 3
    print(i + 1, "-", name)

# 2
print()
for i in range(100):
    for j in range(100):
        print(name, end=" ")
    print()

# 4
print()
for i in range(1, 21):
    print(i, "---", i ** 2)

# 5
print()
for i in range(8, 90, 3):
    print(i, end=",")

# 6
print()
for i in range(100, 0, -2):
    print(i, end=",")

# 7
print()
for i in range(10):
    print("A", end="")
for i in range(7):
    print("B", end="")
for i in range(4):
    print("C", end="")
    print("D", end="")
print("E", end="")
for i in range(5):
    print("F", end="")
print("G", end="")

# 8
print()
name = input("Enter your name: ")
number = int(input("Enter how many times you want to print your name: "))
for i in range(number):
    print(name)

# 9
print()
number = int(input("Enter how many numbers you want to print Fibonacci series: "))
a = 1
b = 1
for i in range(number):
    print(a, end=",")
    a, b = b, a + b

# 10
print()
width = int(input("Enter the width of the box: "))
height = int(input("Enter the height of the box: "))
for i in range(height):
    print("*" * width)

# 11
print()
width = int(input("Enter the width of the box: "))
height = int(input("Enter the height of the box: "))
for i in range(height):
    if i % (height - 1) == 0:
        print("*" * width)
    else:
        print("*", end="");
        print(" " * (width - 2), end="");
        print("*", end="\n")

# 12
print()
height = int(input("Enter the triangle height: "))
for i in range(1, height + 1):
    print("*" * i)
