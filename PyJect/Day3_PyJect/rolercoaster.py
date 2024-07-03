print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm? "))
wants_photo = str()
pcs = int()
bill = 0
invoice = 0
photo_bill = 0

if height >= 120:
    #print("Please proceed to the cashier.")
    age = int(input("What is your Age? "))
    if age <= 12:
        bill = 5
        print("The Price of this class is $5.")
    elif age <= 18:
        bill = 7
        print("The Price of this class is $7.")
    elif age <= 45:
        bill = 12
        print("The Price of this class is $12.")
    else:
        bill = 15
        print("The Price of this class is $15.")

#Input of user: Purchasing Number of Images
    wants_photo = input("Do you want to Purchase Photos? Y or N \n ")
    if wants_photo == "Y" or wants_photo == "y":
        #bill += 3 is the same as bill = bill + 3
        pcs = int(input("How many Pieces do you want? \n"))
        if pcs == 1:        #number of images
            photo_bill = 1  #price of the 4 pieces images
            invoice = bill + photo_bill #computation
            print(f"Your total bill is ${invoice}, Thank you!")
        elif pcs == 2:
            photo_bill = 3
            invoice = bill + photo_bill
            print(f"Your total bill is ${invoice}, Thank you!")
        elif pcs == 3:
            photo_bill = 5
            invoice = bill + photo_bill
            print(f"Your total bill is ${invoice}, Thank you!")
        elif pcs == 4:
            photo_bill = 7
            invoice = bill + photo_bill
            print(f"Your total bill is ${invoice}, Thank you!")
        elif pcs == 5:
            photo_bill = 10
            invoice = bill + photo_bill
            print(f"Your total bill is ${invoice}, Thank you!")
        else:
            print(f"Your total bill is ${bill}, Thank you!")

    else:print(f"Your total bill is ${bill}, Thank you!")

else:
    print("Sorry, you have to grow taller before you can ride.")