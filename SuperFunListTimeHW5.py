#I received assistance from Alyssa Attonito
import string
import math
import numpy

def nested_sum(listA):
    currentSum = 0
    for i in listA:
        if type(i) == list:
            currentSum = currentSum + nested_sum(i)
        else:
            currentSum = currentSum + i
    return currentSum
print(nested_sum([[1,2],[3],[4,5,6]])

def cumulative_sum(listB):
    length = len(listB)
    listC = [0] * length
    currentSum = 0
    i = 0
    while i<length:
        currentSum = currentSum + listB[i]
        listC[i] = currentSum
        i = i +1
    return listC

#print(cumulative_sum([1,2,3,4]))

def middle(listC):
    middle = listC[1:-1]
    return middle
#print(middle([1,2,3,4,5,6,7,8,9]))

def chop(listD):
    listD = listD[1:-1]
    print(listD)
#print(chop([1,2,3,4,5,6,7,8]))


def is_sorted(listE):
    copy = listE.copy()
    listE.sort()
    if listE == copy :
        return True
    else:
        return False
#print(is_sorted(['a','b']))

def is_anagram(wordA, wordB):
   sortedA = sorted(wordA)
   sortedB = sorted(wordB)
   if sortedA == sortedB :
       return True
   return False
#print(is_anagram('grace', 'ecarg'))

def has_duplicates(listF):
    copyList = listF.copy()
    copyList.sort()
    i = 1
    while i < len(listF):
        if(copyList[i-1] == copyList[i]):
            return True
        else:
            i = i + 1
    return False
#print(has_duplicates([1,2,3,5,6]))

