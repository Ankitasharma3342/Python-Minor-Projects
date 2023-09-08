import random

while True:
    user_action = input("Enter a choice(Stone,Paper,Scissor): ")
    possible_action = ["Stone", "Paper", "Scissor"]
    Computer_action = random.choice(possible_action)

    print(f"\nYou choose {user_action},computer choose {Computer_action}.\n")

    if(user_action==Computer_action):
        print("It's a tie")
    elif(user_action=="Stone"):
        if(Computer_action=="Paper"):
            print("Paper covers the stone!  Sorry you lost the game")
        else:
            print("Stone smashes the scissor.  Congrats you won the game")
    elif(user_action=="Paper"):
        if(Computer_action=="Stone"):
           print("Paper covers the stone.  Congrats you won the game")
        else:
           print("scissor cut the paper!   Sorry you lost the game")
    elif(user_action=="Scissor"):
        if(Computer_action=="Paper"):
           print("scissor cut the paper.   Congrats you won the game")
        else:
           print("Stone smashes the scissor!  Sorry you lost the game")
    else:
        print("You choose wrong")

    play_again = input("Play again? (y/n): ")
    if play_again.lower()=="n":
        break

 