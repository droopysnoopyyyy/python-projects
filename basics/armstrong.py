n = int(input("enter a number: "))
count = 0
sum = 0
q = n
while n > 0:
    r = n % 10
    count += 1
    n //= 10
p = count
n = q
while n > 0:
    r = n % 10
    sum += ((r)**p)
    n //= 10
if sum == q:
    print(q, "is an armstrong number")
else:
    print(q, "is not an armstrong number")
