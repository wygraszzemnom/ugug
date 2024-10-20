import random

def game(choice, result):
    print("")
    print("==========hej w tej grze poznasz pana od wf==========")
    computer_choice = random.choice("rps")
    print("--------------------------------------------------------------------")
    print("your choice - ", choice)
    print("computer choice - ", computer_choice)
    if str.lower(choice) == computer_choice:
        print("-----------------------Draw------------------------------")
    elif str.lower(choice) == "r" and computer_choice == "p":
        print("-----------------------computer wins------------------------------")
        result["computer"] += 1
    elif str.lower(choice) == "r" and computer_choice == "s":
        print("-----------------------player wins------------------------------")
        result["player"] += 1
    elif str.lower(choice) == "p" and computer_choice == "s":
        print("-----------------------computer wins------------------------------")
        result["computer"] += 1
    elif str.lower(choice) == "p" and computer_choice == "r":
        print("-----------------------player wins------------------------------")
        result["player"] += 1
    elif str.lower(choice) == "s" and computer_choice == "r":
        print("-----------------------computer wins------------------------------")
        result["computer"] += 1
    elif str.lower(choice) == "s" and computer_choice == "p":
        print("-----------------------player wins------------------------------")
        result["player"] += 1
    else:
        print("error.")


result = {"computer":0, "player":0}   
choice = input("select R/P/S - ")
game(choice=choice, result=result)

