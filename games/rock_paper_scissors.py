import random
print("Rock Paper Scissors Game! >U<")
choices = ["rock", "paper", "scissor"]
name = input("enter your name: ").title()
user = input("enter rock, paper or scissors: ").lower()
comp = random.choice(choices)

if user == comp:
    print("it's a tie!")
elif (user == "rock" and comp == "scissor"):
    print(f"User {name} wins the move {user}!")
elif (user == "paper" and comp == "rock"): 
    print(f"User {name}  wins the move {user}!")   
elif (user == "scissor" and comp == "paper"):
    print(f"User {name}  wins the move {user}!")
else: 
    print(f"Machine wins with the move {comp}!")
