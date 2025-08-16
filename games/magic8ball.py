import random
q = input("Ask The Magic 8 Ball A Question!: ")
magic8 = random.randint(1, 9)
if (magic8 == 1):
    print("Yes - definitely")
elif (magic8 == 2):
    print("It is decidedly so")
elif (magic8 == 3):
    print("Without a doubt")
elif (magic8 == 4):
    print("Reply hazy, try again")
elif (magic8 == 5):
    print("Ask again later")
elif (magic8 == 6):
    print("Better not tell you now")
elif (magic8 == 7):
    print("My sources say no")
elif (magic8 == 8):
    print("Outlook not so good")
elif (magic8 == 9):
    print("Very doubtful")
else:
    print("IDK MAN")
