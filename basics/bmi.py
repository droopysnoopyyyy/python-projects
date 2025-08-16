w = float(input("enter the weight: "))
h = int(input("enter the height (in cms): "))
x = h/100
bmi = w/(x * x)
print("your bmi is: ", bmi)
if (bmi >= 0 and bmi < 18.5):
    print("you're underweight")
elif (bmi >= 18.5 and bmi <= 24.9):
    print("normal body weight")
elif (bmi >= 25.0 and bmi <= 29.9):
    print("overweight")
elif (bmi >= 30.0 and bmi <= 34.9):
    print("obesity (1st class)")
elif (bmi >= 35.0 and bmi <= 39.9):
    print("obesity (2nd class)")
elif (bmi >= 40):
    print("extreme obesity (3rd class)")