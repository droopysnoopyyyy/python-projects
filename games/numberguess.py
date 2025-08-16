x = 5
for i in range(5, 0, -1):
    guess = int(input("guess a number between 1 and 10!: "))
    
    if guess == x:
        print("congratulations! you guessed the number!")
        break
    elif guess > x:
        print("too high")
    else:
        print("too low")

    if i > 1:
        print("no. of attempts left: ", i-1)
    else:
        print("sorry, you've run out of attempts")