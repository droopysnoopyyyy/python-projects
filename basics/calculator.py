def sum(a,b):
    sum = a + b
    print("the sum is: ", sum)
    return "thank you for using this calculator"

def subtraction(a,b):
    diff = a - b
    print("the difference is: ", diff)
    print("thank you for using this calculator")

def multiply (a,b):
    product = a * b
    print("the product is: ", product)
    print("thank you for using this calculator")

def division (a,b):
    div = a/b
    if b != 0:
        print("the quotient is: ", div)
    else:
        print("math error")

    print("thank you for using this calculator")

def square_root(a):
    sqrt = a**0.5
    print("the square root is: ", sqrt)
    print("thank you for using this calculator")

x = int(input("for addition, press 1 \n for subraction, press 2 \n for multiplication, press 3 \n for division, press 4 \n to find out the square root, press 5: "))
if x == 1:
    num1 = int(input("enter the 1st number: "))
    num2 = int(input("enter the 2nd number you want to add to the 1st number: "))
    sum(num1, num2)
elif x == 2:
    num1 = int(input("enter the 1st number you want to find the difference of: "))
    num2 = int(input("enter the 2nd number you want to subtract from the given number: "))
    subtraction(num1, num2)
elif x == 3:
    num1 = int(input("enter the 1st number you want to multiply: "))
    num2 = int(input("enter the 2nd number you want to multiply: "))
    multiply(num1, num2)
elif x == 4:
    num1 = int(input("enter the number you want to divide: "))
    num2 = int(input("enter the number you want to divide it with: "))
    division(num1, num2)
elif x == 5:
    num1 = int(input("enter the number you want to find the square root of: "))
    square_root(num1)
else:
    print("invalid input")
