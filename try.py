# Tax calculator
while True:
    try:
        gross = float(input("How much money do you earn gross ?"))
        children = int(input("How many children do you have?"))
        if gross and children >= 0:
            break
        else:
            print("Enter a positive number")
    except ValueError:
        print("Enter a valid value")
if gross < 1000:
    print(f"Your net salary is {gross - (gross * (0.10-children*0.01))}")
elif gross < 2000:
    print(f"Your net salary is {gross - (gross * (0.12-children*0.01))}")
elif gross < 4000:
    print(f"Your net salary is {gross - (gross * (0.14-children*0.005))}")
else:
    print(f"Your net salary is {gross - (gross * (0.18-children*0.005))}")
