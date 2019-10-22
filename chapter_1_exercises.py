for i in range(4):
    for j in range(19):
        print("*", end="")
    print()

print()
for i in range(4):
    if i % 3 == 0:
        print("*" * 19)
    else:
        print("*", end="");
        print(" " * 17, end="");
        print("*", end="\n")

print()
for i in range(4):
    print("*" * (i + 1))

print()
result = (512 - 282) / (47 * 48 + 5)
print(result)

print()
number = int(input("Enter a number: "))
print("The square of %d is %d" % (number, number ** 2))

print()
number = int(input("Enter a number: "))
print(number, 2 * number, 3 * number, 4 * number, 5 * number, sep="---")
