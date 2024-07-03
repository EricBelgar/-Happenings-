#variables
weeks = 4.34524
month = 0.9999993425
x = 90

#prompt to the user an input of age.
age = input("How long do live before you gets 90? \n Enter your age : ")

#converting input into integer
user_age = int(age)

#calculation how many years left to hit 90 years old.
#Months Calculation
TimeToLive = (x - user_age)

#Weeks Calculation
weeks_to_live = TimeToLive * 52

#Days Calculationi
days_to_live = TimeToLive * 365

print(f"You only have {TimeToLive} years, {weeks_to_live} weeks, or {days_to_live} days to live.")