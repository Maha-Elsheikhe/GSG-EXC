# Exercise 1
num1 = float(input(f"Enter the first number:"))
num2 = float(input(f"Enter the second number:"))

print(f"Sum => {num1 + num2}")
print(f"Subtract => {num1 - num2}")
print(f"Multiply => {num1 * num2}")
print(f"Divide => {num1 / num2}")
print(f"Floor Divide => {num1 // num2}")
print(f"Modulo => {num1 % num2}")
print(f"Power => {num1 ** num2}")

# Exercise 2
text = input("Enter your text statement:")

print(text.upper())
print(len(text))
print(text.split(" "))
print("Python"in text)
print(text[::-1])

# Exercise 3
number = "3.7"

print(f"Convert String To Float => {float(number)}, Type => Float")
print(f"Convert Float To Int => {int(float(number))}, Type => Int")
print(f"Convert Int To String => {str(number)}, Type => String")

# Exercise 4
password = input("Enter Your Password:")

print(f"Longer than 8 characters => {len(password) > 8}")
print(f"Contain uppercase character => {password != password.lower()}")
print(f"Start with a letter => {password[0].isalpha()}")
