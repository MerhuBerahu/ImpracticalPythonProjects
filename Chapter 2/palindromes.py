import sys

file = "chapter 2//2of4brif.txt"
try:
    with open(file,'r') as words: # open 2of4brif.txt as variable words
        words = words.read().strip().split('\n') # create list from contents of words, stripping any spaces and with each index split by \n 
        words = [x.lower() for x in words] # creates a new list from original list 'words; but in lowercase
        for i in words:
            if i[::1] == i[::-1]: #if the order mormaly is the same in revers, print the word
                print(i)


except IOError as e: # if cant open file throw an error rather than crash
    print("{}\nError opening {}. Terminating program.".format(e, file),file=sys.stderr)
    sys.exit(1)

