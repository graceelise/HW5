#received help from Kristina
import os
cwd = os.getcwd()
cwd
file = open('words.txt')

def over20(word):
    if len(word) > 20:
        return True
    else:
        return False
    print(word)

def createWordList():
    newList = []
    file = open('words.txt')
    for word in file:
        newList.append(word[:-1])
    return newList

def over20List():
    file = open('over20List', 'w')
    for word in createWordList():
        if over20(word) == True:
            file.write(word+" ")
        else:
            over20(word) == False

over20List()