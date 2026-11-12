import random 
wins = 0
loses = 0
userPLayChoice = (input("do you want to play rock paper scissors (y/n): "))
while userPLayChoice == "y":
    computerOptions = "RPS"
    computerChoice = random.choice(computerOptions)
    userChoice = (input("type r p or s:  "))
    if computerChoice == "R" and userChoice == "p":
        wins = wins + 1
        print(f"you win you are at {wins} wins and {loses} loses")
    elif computerChoice == "P" and userChoice == "s":
        wins = wins + 1
        print(f"you win you are at {wins} wins and {loses} loses")
    elif computerChoice == "S" and userChoice == "r":
            wins = wins + 1
            print(f"you win you are at {wins} wins and {loses} loses")
    elif computerChoice == userChoice:
                print(f"you drawed you are at {wins} wins and {loses} loses")
    else:
         loses = loses + 1
         print(f"you lose you are at {wins} wins and {loses} loses")
    userPLayChoice = (input("do you want to play rock paper scissors (y/n): "))

