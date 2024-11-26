""" Jimmy Clark
Tex Adventure Editor
A text adventure editor with node editor and save and load in JSON format.
"""

def main():
    file = open("userChoice.txt", "w")
    file.write("0) exit \n")
    file.write("1) load default game \n")
    file.write("2) load a game file \n")
    file.write("3) save the current game \n")
    file.write("4) edit or add a node \n")
    file.write("5) play the current game \n")
    file.close()
    print("Here are your options:")
main()

def main():
    file = open("userChoice.txt", "r")
    for line in file:
        line = line.strip()
        print(format(line))
    file.close()
main()

userChoice = input("Choose an option: ")
getUserChoice = ()
def main():
    keepGoing = True
    while keepGoing:
        userChoice = getUserChoice()
        if userChoice == "0":
            print("goodbye!")
            keepGoing = False
        elif userChoice == "1":
            print("load default game")
            game = getDefaultGame()
        elif userChoice == "2":
            print("load a game file")
        elif userChoice == "3":
            print("saving")
        elif userChoice == "4":
            print("edit or add a node: ")
        elif userChoice == "5":
            print("play the current game")
main()

if userChoice == "4":
    print("Current nodes: start")
    choose = input("Choose node to edit or enter new node name: ")
    menuA = input("Description (Default start node): Do you want to win or lose?: ")
if menuA == "win":
    print("You win!")
if menuA == "lose":
    print("You lose")
else:
    print("Quitting")
    break 

import json

def main():
    option4 = {
        "start": ["Do you want to win or lose?", "I want to win", "win", "I'd rather lose", "lose"],
        "win": : ["You win!", "Start over", "start", "Quit", "quit"],
        "lose": ["You lose!", "Start over", "start", "Quit", "quit"],
        }
    outFile = open("option4.json", "w")
    json.dump (option4, outFile, indent=2)
    outFile.close()
    print("saved Option 4 data to option4.json")
main()
    
        