# Exercise 1
print("#### Temperature toolkit ####")


def celsius_to_fahrenheit(c):

    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f):

    return (f - 32) * 5 / 9


def celsius_to_kelvin(c):

    return c + 273.15


print(celsius_to_fahrenheit(30))
print(fahrenheit_to_celsius(30))
print(celsius_to_kelvin(30))

# Exercise 2
print("#### String utilities ####")


def is_palindrome(text):

    text = text.replace(" ", "").lower()
    return text == text[::-1]


print(is_palindrome("A man a plan a canal Panama"))

# Exercise 3
print("#### Grade statistics ####")


def analyse_grades(grades):

    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)
    passed = 0

    for grade in grades:
        if grade >= 60:
            passed += 1

    print("Average : ", average)
    print("Highest grade : ", highest)
    print("Lowest grade : ", lowest)
    print("Number of passed students : ", passed)


grades = [85, 72, 58, 90, 45, 67]
analyse_grades(grades)

# Exercise 4


def calculate_factorial(number):
    """
    Calculate and return the factorial of a positive number
    """
    result = 1

    for i in range(1, number + 1):

        result *= i

    return result


def main():
    """
    Ask the user for a number and print its factorial
    """
    number = int(input("Enter a number: "))
    factorial = calculate_factorial(number)
    print(f"Factorial = {factorial}")


main()
