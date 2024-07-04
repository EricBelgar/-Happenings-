# Our mission is to find the magical treasure and give to the community.

#Declaration of variables



print("Welcome to the Treasure Island. \nYour mission is to find The Magical Treasure.\n")
#print("On a journey there is a path headed to 2 ways, left side is a messy woods,\nfull of wild creatures and wilderness. while the other one there is a light \nthat forcasted the new beginning and luxurious life")

path = (input("Which path do you want to go with? \n a. Left - Dark, Wilderness with unknown Beast. \n b. Right - Life for New Beginning with luxurious life. \n"))
if path == "a" or path == "A":
    path_a = input("What do you want to?\n a. Swim \n b. Ride\n")
    if path_a == "a" or path_a == "A":
        print("Thanks you for Playing :) \n GAME OVER!!")
    elif path_a == "b" or path_a == "B":
        print("Welcome to the Road of the Tricksters.")
        Road_answer_c = input("Pick one of the Roads\n a. Road to Asphodel\n b. Swampy Abyss\n c. Road to Tartarus\n")
        if Road_answer_c == "a" or Road_answer_c == "a":
            print("Paradise for Normal peaple?\nYou're wrong!! Game Over!!!!!")
        elif Road_answer_c == "b" or Road_answer_c == "B":
            print("HAHAHHAHAH, Ride to Swampy Abyss? Good Luck!!! Game Over")
        elif Road_answer_c == "c" or Road_answer_c == "C":
            doors_answer = input("Congrats you picked the right path, Now pick one\n a. Gate of Trials\n b. Heavens Arena\n")
            print("Congratulations!!!! You found the One Piece.")
        else:
            print("Thank you for Playing. \nYOU ARE GAME OVER!!!")
elif path =="b" or path == "B":
    print("Thank you for Playing. Have a LUXURIOUS LIFE. \nYOU ARE GAME OVER!!!")

else:
    print("Thank you for Playing. \nYOU ARE GAME OVER!!!")