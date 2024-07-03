#which year do you want to check?
year = int(input("Enter year to check if its Leap Year or Not. \n "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is Leap Year")
        else:
            print(f"{year} is Not Leap Year")
    else:
        print(f"{year} is Leap Year")
else:
    print(f"{year} is Not Leap Year")