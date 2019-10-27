# 1
input_ = input("Enter a string: ")
# a
print(len(input_))
# b
print(input_ * 10)
# c
print(input_[0])
# d
print(input_[:3])
# e
print(input_[len(input_) - 3:len(input_)])
# f
print(input_[len(input_)::-1])
# g
if len(input_) >= 7:
    print(input_[6])
else:
    print("The string is not long enough to print that character")

#h
removed_string=input_[1:len(input_)-1]
print(removed_string)
#i
print(input_.upper())
#j
print(input_.replace("a","e"))
#k
print(input_.replace(input_," "))