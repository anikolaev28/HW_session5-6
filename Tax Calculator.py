#Tax calculator using if function
print("Welcome to your tax calculator")
while True:
    try:
        gross = float(input("How much money do you earn gross?"))
        if gross > 0:
            break
        else:
            print("The gross salary must be positive")
    except ValueError:
            print("Invalid input. Please enter a valid number.")
while True:
    try:
        child = int(input("How many children do you have?"))
        if child >= 0:
            break
        else:
            print("The number of children must be positive")
    except ValueError:
            print("Invalid input. Please enter a valid number.")
if gross < 1000:
    print(f"Your net salary is {gross - (gross * (0.10-child*0.01))}")
elif gross < 2000:
    print(f"Your net salary is {gross - (gross * (0.12-child*0.01))}")
elif gross < 4000:
    print(f"Your net salary is {gross - (gross * (0.14-child*0.005))}")
else:
    print(f"Your net salary is {gross - (gross * (0.18-child*0.005))}")
