#1
cm=int(input("Enter a length in centimeters: "))
if cm<0:
    print("Length cannot be negative!")
else:
    print("Centimeters: %d, Inches: %.2f" %(cm,cm/2.54))

#2
print()
temperature=float(input("Enter a temperature: "))
selection=int(input("Which unit you want to use?\n1. Celsius\n2. Fahrenheit\n"))
if selection==1:
    print("The temperature in Fahrenheit is",(9/5)*temperature+32)
if selection==2:
    print("The temperature in Celsius is", (5/9)*(temperature-32))

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

