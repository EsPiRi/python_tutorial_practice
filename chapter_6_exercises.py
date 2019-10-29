# 1
from collections import *

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

# 5
print()
string = input("Enter a string: ")
new_string = string.replace(string[1], "*")
print(new_string + "!!!")

# 6
print()
s = input("Enter your string: ")
s = s.lower()
s = s.replace(".", "")
s = s.replace(",", "")
print(s)

# 7
print()
word = input("Enter your word: ").lower()
reverse_word = word[len(word)::-1].lower()
if word == reverse_word:
    print("Palindrome")
else:
    print("Not palindrome")

# 8
print()
number_of_input = int(input("Enter how many entries will be entered: "))
e_mails = list()
professor_mail = False
for i in range(number_of_input):
    new_e_mail = input()
    e_mails.append(new_e_mail)
    if new_e_mail.__contains__("@prof.college.edu"):
        professor_mail = True

if professor_mail:
    print("Some professor mail has entered.")
else:
    print("All mails are student e-mails.")

# 9
print()
number = int(input("Enter a number: "))
for i in range(1, number + 1):
    print(" " * i + str(i))

# 10
print()
string = input("Enter a string: ")
for i in string:
    print(i * 2)

# 11
print()
word = input("Enter a word contains 'a' letter: ")
for i in word:
    if i in ["a", "A"]:
        print(i)
    else:
        print(i, end="")

# 12
print()
word = list(input("Enter a word: "))
for i in range(len(word)):
    if i % 2 == 1:
        word[i] = word[i].upper()

new_word = "".join(word)
print(new_word)

# 13
print()
str_1, str_2 = input("Enter a string: "), input("Enter a string with the same length as the previous one: ")

if len(str_1) == len(str_2):
    for i in range(len(str_1)):
        print(str_2[i], end="")
        print(str_1[i], end="")
else:
    print("The length of two inputs are not equal!")

# 14
print()
name = list(input("Enter your name in lowercase: ").split())
print(name)
for i in range(len(name)):
    temp = list(name[i])
    temp[0] = temp[0].upper()
    name[i] = "".join(temp)

name = " ".join(name)
print(name)

#15
print()
college_class=input("Enter a college class: ")
adjective=input("Enter an adjective: ")
activity=input("Enter an activity: ")

formatted_story=college_class+" class was really "+adjective+" today. We learned how to "+activity+" today in class. I can't wait for tomorrow's class!"

print(formatted_story)

# 16
name, surname = input("Enter name: ").split()

print("Dear %s %s, I am pleased to offer you our new Platinum Plus Rewards card at a special introductory APR of 47.99%%. %s, an offer like this does not come along every day, so I urge you to call now toll-free at 1-800-314-1592. We cannot offer such a low rate for long, %s, so call right away." %(name,surname,name,name))


#17
print()
char=deque(list(map(chr,range(97,123))))

for i in range(len(char)):
    print("".join(char))
    char.rotate(-1)

#18
#a
print()
string=input("Enter a string: ")
letter=input("Enter a letter: ")
if string.__contains__(letter):
    print("This string contains this letter.")
else:
    print("This string doesnt contain this letter.")

#b
print()
string=input("Enter a string: ")
letter=input("Enter a letter: ")
letter_count=0
for i in string:
    if i==letter:
        letter_count+=1

print(letter_count)

# c
print()
string = input("Enter a string: ")
letter = input("Enter a letter: ")
index = -1
for i in range(len(string)):
    if string[i] == letter:
        index = i
        break

if index != -1:
    print("First occurence in", index, "index")
else:
    print("The letter doesnt occur in this string.")


# 19
print()
number = list(input("Enter a large integer (e.g 1 million)"))
new_number=""
if len(number) % 3 == 0:
    for i in range(len(number)):
        if (i%3==2)&(i<len(number)-1):
            new_number+=number[i]+","
        else:
            new_number+=number[i]

elif len(number)%3==1:
    new_number+=number[0]+","
    for i in range(1,len(number)):
        if (i%3==0)&(i<len(number)-1):
            new_number+=number[i]+","
        else:
            new_number+=number[i]
elif len(number)%3==2:
    new_number+=number[0]+number[1]+","
    for i in range(2,len(number)):
        if (i%3==1)&(i<len(number)-1):
            new_number+=number[i]+","
        else:
            new_number+=number[i]

print(new_number)