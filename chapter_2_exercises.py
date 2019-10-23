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
