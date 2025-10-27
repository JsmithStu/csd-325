# ---------------------------------------------
# Name: Johnathan Smith
# Course: CSD 325 - Advanced Python
# Assignment: Module 1 - On the Wall
# Date: October 26 2025
# This program asks the user how many bottles of beer
# are on the wall, then counts down using the classic
# "Bottles of Beer on the Wall" song structure.

def beer_song(bottles):
    for i in range(bottles, 0, -1):
        if i == 1:
            print(str(i) + " bottle of beer on the wall")
            print(str(i) + " bottle of beer")
            print("Take one down, pass it around")
            print("No more bottles of beer on the wall\n")
        else:
            print(str(i) + " bottles of beer on the wall")
            print(str(i) + " bottles of beer")
            print("Take one down, pass it around")
            print(str(i - 1) + " bottles of beer on the wall\n")
    print("Time to buy more beer!")


# Main program
bottles = int(input("Enter number of bottles: "))
beer_song(bottles)
