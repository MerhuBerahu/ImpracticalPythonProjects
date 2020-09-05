import random
import sys # imported for red text

first = open("chapter 1//first.txt",'r') # open first.txt in read mode and assign to variable first
last = open("chapter 1//last.txt", 'r')# open last.txt in read mode and assign to variable last
first = first.read().split(",") # create list from contents of first, with each index split by ,
last = last.read().split(",") # create list from contents of last, with each index split by ,


def randnames(): # create and return a random name
    random_first = random.choice(first)
    random_last = random.choice(first)
    name = random_first + " " + random_last
    return name

while True: # lopp to generate random names till user quits
    print(f"Random Name = {randnames()}", file=sys.stderr) #meant to be in red
    try_again = input("Press 'Enter' to generate a new random name or 'exit' to quit ")
    if try_again.lower() == "exit":
        sys.exit(0)