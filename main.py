# Exercise 1
# import random

# names = ['Alice', 'Bob', 'Charlie', 'David']
# choice = random.choice(names)
# print("Randomly selected name:", choice)

# Exercise 2
from datetime import datetime

current_time = datetime.now()
print("Current date and time:", current_time.strftime("%Y-%m-%d"))
print("Current date and time:", current_time.strftime("%d %B %Y"))
print("Current date and time:", current_time.strftime("%A %B %d %Y %I:%M:%S %p"))

# Exercise 3
from pathlib import Path

fileName = input("Enter a file name: ")
file_path = Path("example") / fileName
if file_path.exists():
    print("File exists.")
else:
    print("File does not exist.")

# Exercise 4
from grade_utils import calculate_grade, passed

print("Grade for score 85:", calculate_grade(85))
print("Did the student pass with score 85?", passed(85))

# Exercise 5
# "pip install requests" in terminal to install requests library
import requests

# send a GET request to Github API to receive a response
response = requests.get("https://api.github.com/events")
# converts the JSON response from the API into python data structures (dictionary, list, etc)
print(response.json())
