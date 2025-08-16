str1 = input("enter the 1st string: ")
str2 = input("enter the 2nd string: ")
str1 = str1.lower()
str2 = str2.lower()
x = []
y = []
if (len(str1) == len(str2)):
    for a in str1:
        x.append(a)
    x.sort()
    for a in str2:
        y.append(a)
    y.sort()
    print(x)
    print(y)
    if (x == y):
        print("The Two Strings Are Anagrams")
    else:
        print("The Two Strings Are Not Anagrams")