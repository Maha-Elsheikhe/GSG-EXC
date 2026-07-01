# Exercise 1
with open("notes.txt", "w") as file:
    file.write("First line\n")
    file.write("Second line\n")
    file.write("Third line\n")

with open("notes.txt", "r") as file:
    for line in file:
        print(line, end="")

# Exercise 2
action = input("Enter an action: ")

with open("activity_log.txt", "a") as file:
    file.write(action + "\n")


# Exercise 3
def get_number(question):
    while True:
        user_input = input(question)
        try:
            return int(user_input) 
        except ValueError:
            print("Invalid input. Please enter a valid number.")

get_number("Enter an integer number: ")


# Exercise 4
import csv

total = 0
count = 0

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total += float(row["score"])
        count += 1

if count > 0:
    average = total / count
    print("Average score:", average)
else:
    print("No scores found.")

# Exercise 5

# FileNotFoundError
try:
    open("non_existent_file.txt", "r")
except FileNotFoundError:
    print("File not found.")

# ValueError
try:
    int("not_a_number")
except ValueError:
    print("Invalid value.")

# KeyError
my_dict = {"key1": "value1"}
try:
    print(my_dict["key2"])
except KeyError:
    print("Key not found in dictionary.")

