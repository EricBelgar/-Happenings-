import random

namesSplit = str(input("Who's gonna pay the bill? \n"))

names = namesSplit.split(", ")

banker = len(names)

random_choice = random.randint(0, banker - 1)

print(f"{names[random_choice]} Thanks for tha meal. <3")

#print(banker)
#banker = input("Who's gonna pay the bill? ")
