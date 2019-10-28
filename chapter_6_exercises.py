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

# h
removed_string = input_[1:len(input_) - 1]
print(removed_string)
# i
print(input_.upper())
# j
print(input_.replace("a", "e"))
# k
print(input_.replace(input_, " "))

# 2
print()
sentence = input("Enter a text: ")
print(sentence.count(" ") + 1)

# 3
print()
formula = input("Enter a formula: ")
opening_parenthesis = formula.count("(")
closing_parenthesis = formula.count(")")
if opening_parenthesis == closing_parenthesis:
    print("Same number of parenthesis")
else:
    print("Different number of parenthesis", opening_parenthesis, closing_parenthesis)

# 4
print()
word = input("Enter a word: ")
contains_vowel = False
for letter in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
    if letter in word:
        contains_vowel = True

if contains_vowel:
    print("This word contains at least one vowel.")
else:
    print("This word doesn't contain any vowel")

#5
print()
string=input("Enter a string: ")
new_string=string.replace(string[1],"*")
print(new_string+"!!!")

#6
print()
s=input("Enter your string: ")
s=s.lower()
s=s.replace(".","")
s=s.replace(",","")
print(s)
