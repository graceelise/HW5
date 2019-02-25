#I did this by myself
from string import *
import math
import random

def createBirthday(classSize):
    #classSize = input("What is the class size?\n")
    #classSize = int(classSize)
    birthdays = []
    for x in range(classSize):
        birthdays.append(random.randint(1,365))
    return birthdays

#print(createBirthday(23))

def findMatches():
    birthdays = createBirthday(23)
    #print(birthdays)
    i = 0
    n = 1
    length = len(birthdays)
    currentVal = birthdays[i]
    while i < length:
        while n < length:
            if(birthdays[i] == birthdays[n]):
                #print('birthday = ' + str(birthdays[i]) + " is the same as " + str(birthdays[n]))
                return True
                break
            else:
                n = n + 1
        i = i + 1
        n = i + 1
    return False

#print(findMatches())

def testProbability(classSize):
    numTests = input('how many tests should I run?\n')
    numTests = int(numTests)
    #classSize = input("what class size?\n")
    #classSize = int(classSize)
    numTrue = 0

    i = 0
    while i < numTests :
        birthdays = createBirthday(classSize)
        if(findMatches() == True):
            numTrue = numTrue + 1
        i = i + 1
    print(numTrue)
    numTrueP = numTrue/numTests
    return numTrueP

print(testProbability(23))
