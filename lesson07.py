# Exercise 1
print(f"###Season Detector###")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
try:
    month = int(input("Enter a month number (1-12):"))
except ValueError:
    month = None

if month in numbers:
    if month == 1 or month == 2 or month == 12:
        print("Summer ")
    elif 3 <= month <= 5:
        print("Autumn")
    elif 6 <= month <= 8:
        print("Winter")
    elif 9 <= month <= 11:
        print("Spring")
else:
    print("Invalid Month Number!")

# Exercise 2
print("####BMI Calculator####")
try:
    weight = float(input("Enter weight:"))
    height = float(input("Enter height:"))
except ValueError:
    weight = None
    height = None

if weight is None or height is None:
    print("Weight and height must be numeric values!")
elif weight > 0 and height > 0:
    bmi = weight / (height**2)
    if bmi <= 18.5:
        print("Underweight")
    elif bmi <= 24.9:
        print("Normal")
    elif bmi <= 29.9:
        print("Overweight")
    else:
        print("Obese")
else:
    print("Weight and height must be greater than 0!")


# Exercise 3
print("###Electricity Bill###")
try:
    kwh = float(input("Enter kWh consumed:"))
except ValueError:
    kwh = None
bill = 0

if kwh is None:
    print("kWh consumed must be a numeric value!")
elif kwh < 0:
    print("kWh consumed cannot be negative!")
elif kwh <= 100:
    bill = kwh * 0.40
elif kwh <= 300:
    bill = (100 * 0.40) + ((kwh - 100) * 0.65)
else:
    bill = (100 * 0.40) + (200 * 0.65) + ((kwh - 300) * 0.95)

if kwh is not None and kwh >= 0:
    print(f"Bill Total: R${bill:.2f}")

# Exercise 4
print("#####Rock, Paper, Scissors#####")

player = input("Enter your choice (rock, paper, scissors): ").lower()

computer = "rock"

if player == computer:
    print("It`s tie !")
elif player == "paper":
    print("You win! Paper covers rock.")
elif player == "scissors":
    print("Computer wins! Rock crushes scissors.")
else:
    print("Invalid input!")
