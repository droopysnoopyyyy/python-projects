first = input("enter your first name: ").title()
num = int(input("enter 0 if you've a middle name, 1 if you don't: "))
if num == 0:
    middle = input("enter your middle name: ").title()
    last = input("enter your last name: ").title()

    for char in first:
        if char.isupper():
            first_final = char
            break

    for char in middle:
        if char.isupper():
            middle_final = char
            break

    print("your name is: ", first_final + ". " + middle_final + ". " + last)
else:
    last = input("enter your last name: ").title()
    for char in first:
        if char.isupper():
            first_final = char
            break
    print("your name is: ", first_final + ". " + last)