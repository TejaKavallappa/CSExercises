__author__  = "Teja Kavallappa"

def countWords(str):
    """ Counts the number of space delineated words in a given string"""
    if(str == None):
        return 0;
    numWords = 0
    inWord = False
    for c in str:
        if(c == ' ' and inWord == True):
            inWord = False
            numWords += 1
        elif (c != ' '):
            inWord = True
    return numWords+1


fileName = "./../vanillatext.txt" 
count = 0
with open(fileName) as f:
    for line in f:
        count += countWords(line)
print "Number of words in %s  = %d" %(fileName, count)    

