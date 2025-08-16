import math
rc = 0
hf = 0
gd = 0
sl = 0
print("Q1) Do you like Dawn or Dusk? 1) Dawn 2) Dusk: ")
q1 = int(input("enter your answer (1-2): "))
if (q1 == 1):
    rc += 1
    gd += 1
elif(q1 == 2):
    hf += 1
    sl += 1
print("Q2) When I am dead, I want people to remember me as: 1) The Good 2) The Great 3) The Wise 4) The Bold: ")
q2 = int(input("enter your answer (1-4): "))
if (q2 == 1):
    hf += 2
elif(q2 == 2):
    sl += 2
elif(q2 == 3):
    rc += 2
elif(q2 == 4):
    gd += 2
else:
    print("Wrong input")
print("Q3) Which kind of instrument most pleases your ear? 1) The violin 2) The trumpet 3) The piano 4) The drum: ")
q3 = int(input("enter your answer (1-4): "))
if (q2 == 1):
    sl += 4
elif(q2 == 2):
    hf += 4
elif(q2 == 3):
    rc += 4
elif(q2 == 4):
    gd += 4
else:
    print("Wrong input")

print("Gryffindor: ", gd)
print("Hufflepuff: ", hf)
print("Ravenclaw: ", rc)
print("Slyterin: ", sl)

r = max(hf, sl, gd, rc)
print(r)
if (r == hf):
    print("HUFFLEPUFF")
elif (r == sl):
    print("SLYTHERIN")
elif(r == gd):
    print("GRYFFINDOR")
elif (r == rc):
    print("RAVENCLAW")
else:
    print("NAH")