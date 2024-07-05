import random
random_pick = str()
toss = (str(input("Please pick from Heads and Tails? \n")))
if toss == "Heads":
    toss = 1
    random_pick = random.randint(0,1)
    if random_pick == 1:
        print("Heads")
        if random_pick != toss:
            print("Sorry, Better luck next time!")
        elif random_pick == toss:
            print("You Win!")
        else:
            quit()
    elif random_pick == 0:
        print("Tails")
        if random_pick != toss:
            print("Sorry, Better luck next time!")
        elif random_pick == toss:
            print("You Win!")
        else:
            quit()
    else:
        pass
elif toss == "Tails":
    toss = 0
    random_pick = random.randint(0, 1)
    if random_pick == 1:
        print("Heads")
        if random_pick != toss:
            print("Sorry, Better luck next time!")
        elif random_pick == toss:
            print("You Win!")
        else:
            quit()
    elif random_pick == 0:
        print("Tails")
        if random_pick != toss:
            print("Sorry, Better luck next time!")
        elif random_pick == toss:
            print("You Win!")
        else:
            quit()
    else:
        quit()
else:
    pass
