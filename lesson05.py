# Exercise 1 : Print types of variables in python

number = 10 
float_number = 3.14
text = "Maha Elsheikhe"
boolean_value = True

print("*" * 20)
print("Exercise 1 : Data Types in Python")
print(f"Integer: {number}")
print(f"Float: {float_number}")
print(f"Text: {text}")
print(f"Boolean: {boolean_value}")
print("*" * 30)

# Exercise 2 : Calculate Area and Perimeter of a Rectangle

print("Exercise 2 : Calculate Area and Perimeter of a Rectangle")

# Ask the user for the width and height of the rectangle
width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))

area = int(width) * int(height)
perimeter = 2 * (int(width) + int(height))

print(f"The area of the rectangle is: {area}")
print(f"The perimeter of the rectangle is: {perimeter}")
print("*" * 30)

# Exercise 3: Convert Celsius to Fahrenheit

print("Exercise 3 : Temperature Converter")
# Ask the user for a temperature in Celsius and convert it to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")
print("*" * 30)



