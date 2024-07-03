#Opening remarks or Greetings
print("Welcome to the Tip Calculator")

#input of users bill
bill = float(input("What is your total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
num_of_person = int(input("How many people to split the bill? "))

#calculation of percentage and dividents
Tpercent = (tip / bill) * 100 + bill
divident = float(round(Tpercent / num_of_person, 2))

print(f"The total value that you've spent is {divident}")


