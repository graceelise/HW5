import os
cwd = os.getcwd()
cwd
file = open("words.txt")

def noE(w):
    for letter in w:
        if letter == 'e':
            return False
    return True

def makeWordList():
    newList = []
    file = open("words.txt")
    for line in file:
        newList.append(line[:-1])
    return newList

def printWords():
    eNum = 0
    noENum = 0
    file = open('no_e_list', 'w')
    for word in word_list:
        if noE(word) == True:
            file.write(word)
            noENum += 1
        elif noE(word) == False:
            eNum += 1
    return((noENum / (noENum + eNum) * 100))

makeWordList()
wordList = makeWordList()
print(wordList[0:10])
print(printWords())