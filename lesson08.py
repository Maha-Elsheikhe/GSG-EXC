# Exercise 1
print("#### FizzBuzz ####")
for num in range(1, 51):
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
print("#### End ####")

# Exercise 2
print("#### Fum of digits ####")
number = int(input("Enter a number: "))
total = 0

for digit in str(abs(number)):
    total += int(digit)
print(total)
print("#### End ####")

# Exercise 3
print("#### Password generator preview ####")
for n in range(1, 101) :
    if n % 2 == 0 and n ** 0.5 % 1 == 0 :
        print(n)
print("#### End ####")

# Exercise 4
print("#### ATM Simulation ####")
balance = 1000
choose_list = f"Choose: \n 1. Check balance \n 2. Deposit \n 3. Withdraw \n 4. Exit"

while True : 
    print(choose_list)
    try:
        choose = int(input("Enter your choice (1, 2, 3, 4): "))
    except ValueError:
        print("Invalid choice, Try again...")
        continue
    if choose == 1:
        print("*" * 70)
        print(f"Your balance is now: {balance}")
        print("*" * 70)
        continue
    elif choose == 2:
        try:
            amount = int(input("Enter the amount to deposit: "))
        except ValueError:
            print("Invalid amount")
            continue
        if amount <= 0:
            print("Deposit amount must be greater than 0")
            continue
        balance += amount
        print("*" * 70)
        print(f"Your balance is now: {balance}")
        print("*" * 70)
        continue
    elif choose == 3:
        try:
            amount = int(input("Enter the amount to withdraw: "))
        except ValueError:
            print("Invalid amount")
            continue
        if amount <= 0:
            print("Withdrawal amount must be greater than 0")
            continue
        if amount > balance:
            print("Insufficient balance")
            continue
        balance -= amount
        print("*" * 70)
        print(f"Your balance is now: {balance}")
        print("*" * 70)
        continue
    elif choose == 4:
        print("Thank you for using the ATM")
        break
    else:
        print("Invalid choice, Try again...")
        continue
print("#### End ####")


# Exercise 5 
print("#### Grade Report ####")
grades = {
    "Alice": 92,
    "Bruno": 78,
    "Carla": 85,
    "Daniel": 59
}
avg = 0

for name, grade in grades.items():
    if(grade >= 60) :
      print(f"{name}: {grade} => Passed")
    else:
      print(f"{name}: {grade} => Failed")
    avg += grade

avg /= len(grades)
print(f"Average grade: {avg}")
print("#### End ####")
