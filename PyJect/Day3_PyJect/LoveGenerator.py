# It will check the inputed name by the user if it matches to the word T,R,U,E, L,O,V,E
# it will convert into points and matches to the equivalent status.

# Use count() function to check the given letters.
# Use lower() function to organize the letters and make all the input into lower case letters.

print("Welcome to the Love Calculator!! Lets calculate your score.")
name1 = str(input("What is your Name?\n"))
name2 = str(input("What is their Name?\n"))

# this statement combined the input of the user ex. Eric + LIZA = EricLIZA
combined_names = name1 + name2

# this statement convert the result above (combined_names) into lower case
lowered_names = combined_names.lower()

# at this section it will check the combined_names if it matches to the first_digit (t,r,u,e)
t = lowered_names.count("t")
r = lowered_names.count("r")
u = lowered_names.count("u")
e = lowered_names.count("e")

first_digit = t + r + u + e

l = lowered_names.count("l")
o = lowered_names.count("o")
v = lowered_names.count("v")
e = lowered_names.count("e")

second_digit = l + o + v + e

combined_score = int(str(first_digit) + str(second_digit))

print(combined_score)
if combined_score >= 1 and combined_score <= 50:
    print(f"Your love score is {combined_score}.\nGo buy Roses and Chocolates and give it!!")

elif combined_score >= 51 and combined_score <= 99:
    print(f"Your love score is {combined_score}.\n Get merried and make babies!!")

else:
    print(f"Your love score is {combined_score}. You are a legend!!")
