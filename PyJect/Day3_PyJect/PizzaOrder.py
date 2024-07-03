# Direction:
# ask the costumer what size want to. Small, Medium, and Large.
# Small = 10, medium = 15, Large = 20

# ask the custumer for add ons. like pepperoni and cheese
# pepperoni = $2, cheese = $3

# greetings to the user using print function
print("+---------------------»»——⍟——««-------------------------+")
print("|   Thank you for choosing Python Pizza Deliveries!!    |")
print("+---------------------»»——⍟——««-------------------------+")

bill = 0
pep_sum = 0
psize = str(
    input("What Size of Pizza do you want?\n \"S\" - Small - $10\n \"M\" - Medium - $15\n \"L\" - Large - $20\n"))
add_cheese = str()

if psize == "S" or psize == "s":
    bill = 10
elif psize == "M" or psize == "m":
    bill = 15
elif psize == "L" or psize == "l":
    bill = 20
else:
    print("Thanks for visiting")

add_pepperoni = str(input("Do you want Pepperoni? \"Y\" - Yes, \"N\" - No : "))
if add_pepperoni == "Y" or add_pepperoni == "y":
    pepperbill = 2
    pep_sum = bill + pepperbill
elif add_pepperoni == "N" or add_pepperoni == "n":
    bill = bill
else:
    print(add_cheese)

add_cheese = str(input("Do you want to Add Cheese?\"Y\" - Yes, \"N\" - No : "))
if add_cheese == "Y" or add_cheese == "y":
    cheesebill = 3
    reciept = pep_sum + cheesebill
    print(f"Your total bill is {reciept}")
elif add_cheese == "N" or add_cheese == "n":
    bill = bill
    print(f"Your total bill is {bill}")
else:
    print(f"Your total bill is {bill}")
