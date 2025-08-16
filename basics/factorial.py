def factorial(n):
    f = 1
    for i in range(1, n+1):
        f = f*i
    print("factorial of ", n, "is: ", f)
    return f

num = int(input("enter a number: "))
factorial(num)