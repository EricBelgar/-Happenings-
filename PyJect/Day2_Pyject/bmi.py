
#classifying of variable
height = input("What is your Height in meters? e.g:1.72 : ")
weight = input("What is your Weight in Kilograms? e.g: 50 : ")

#converting inputs into integer and float.
height_in_float = float(height)
weight_in_float = float(weight)

#Calculation of inputs
bmi = round((weight_in_float / height_in_float ** 2), 2)

#printing result
print(bmi)

if bmi <= 18.5:
    print(f"Your BMI is {bmi}, you are Underweight")
elif bmi <= 25:
    print(f"Your BMI is {bmi},you have a Normal Weight.")
elif bmi <= 30:
    print(f"Your BMI is {bmi}, you are Slightly Overweight.")
elif bmi <= 35:
    print(f"Your BMI is {bmi}, you are Obese")
else:
    print(f"Your BMI is {bmi}, you are Clinically Obese.")