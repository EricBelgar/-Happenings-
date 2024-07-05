import random
#import import_module #this section is where you can call the other python file on the code
#print(import_module.pi) #this is how you call the module.


random_integer = random.randint(1, 10) #this section will picked the computer randomly from 1 to 10
print(random_integer)

random_float = random.random() * 5 #will picked random float number from 0.0 to 0.999999 but using "*" it will increase from 0.9999 to 4.999999
print(random_float)

love_score = random.randint(0, 100)
print(f"Your love score is {love_score}")