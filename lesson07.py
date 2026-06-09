# Exercise 1
print(f"###Season Detector###")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
month = int(float(input("Enter a month number (1-12):")))

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
weight = float(input("Enter weight:"))
height = float(input("Enter height:"))

if weight > 0 and height > 0:
    BMI = weight / (height**2)
else:
    print("Error Division by zero is not allowed!")

if BMI <= 18.5:
    print("Underweight")
elif BMI <= 24.9:
    print("Normal")
elif BMI <= 29.9:
    print("Overweight")
else:
    print("Obese")


# Exercise 3
print("###Electricity Bill###")
kwh = float(input("Enter kWh consumed:"))
bill = 0

if kwh <= 100:
    bill = kwh * 0.40
elif kwh <= 300:
    bill = (100 * 0.40) + ((kwh - 100) * 0.65)
else:
    bill = (100 * 0.40) + (200 * 0.65) + ((kwh - 300) * 0.95)

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
