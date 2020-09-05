import random
import sys # imported for red text

try:
    with open("chapter 1//first.txt",'r') as first: # open first.txt in read mode and assign to variable first
        first = first.read().split(",") # create list from contents of first, with each index split by ,
    with open("chapter 1//last.txt", 'r') as last:# open last.txt in read mode and assign to variable last
        last = last.read().split(",") # create list from contents of last, with each index split by ,
except IOError as e:
    print("{}\nError opening {}. Terminating program.".format(e, file),file=sys.stderr)
    sys.exit(1)



def randnames(): # create and return a random name
    random_first = random.choice(first)
    random_last = random.choice(first)
    name = random_first + " " + random_last
    return name

while True: # lopp to generate random names till user quits
    print(f"Random Name = {randnames()}", file=sys.stderr) #meant to be in red
    try_again = input("Press 'Enter' to generate a new random name or type 'exit' first to quit ")
    if try_again.lower() == "exit":
        sys.exit(0)