#  File: sorting.py
#  Description: Tests speeds of various sort functions
#  Student's Name: William Sears
#  Student's UT EID: wvs92
#  Course Name: CS 313E 
#  Unique Number: 50940
#
#  Date Created: 11/16
#  Date Last Modified: 11/17


import random
import time
import sys
sys.setrecursionlimit(10000)

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)
        sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap

        alist[position] = currentvalue

def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1

def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


########################################################

def testSort(sortFunction, aList):


    #Sorted Code

    #print(aList)
    timeList = []
    #print(aList)
    

    for i in range(5):
        startTime = time.perf_counter()
        #print(startTime)
        sortFunction(aList)
        endTime = time.perf_counter()
        #print(endTime)
        elapsedTime = endTime - startTime
        timeList.append(elapsedTime)
        
        

    avgTimeSorted = sum(timeList) / 5
    avgTimeSortedF = '{:f}'.format(avgTimeSorted)


    #Random Code


    timeList = []

    #print(aList)

    random.shuffle(aList)


    #print(aList)
    

    for i in range(5):
        startTime = time.perf_counter()
        #print(startTime)
        sortFunction(aList)
        endTime = time.perf_counter()
        #print(endTime)
        elapsedTime = endTime - startTime
        timeList.append(elapsedTime)
        
        

    avgTimeRandom = sum(timeList) / 5
    avgTimeRandomF = '{:f}'.format(avgTimeRandom)

    #Reverse Code

    #print(aList)
    
    aList.sort()
    print(aList)
    aList.reverse()
    print(aList)

    #print(aList)

    timeList = []
    

    for i in range(5):
        startTime = time.perf_counter()
        #print(startTime)
        sortFunction(aList)
        endTime = time.perf_counter()
        #print(endTime)
        elapsedTime = endTime - startTime
        timeList.append(elapsedTime)
        
        

    avgTimeReverse = sum(timeList) / 5
    avgTimeReverseF = '{:f}'.format(avgTimeReverse)
    print(aList)

    #Almost Sorted Code

    
    aList.sort()
    timeList = []

    #print(aList)

    almostShufNum = int(len(aList) * .1)
    #print (almostShufNum)
    resIndexList = []
    #print( "List's length is:", len(aList))

    for i in range (almostShufNum):
        randomIndex = random.randint(0,len(aList) -1)
        randomIndex2 = random.randint(0,len(aList) -1)
        while randomIndex == randomIndex2:
            randomIndex = random.randint(0,len(aList) -1)
            randomIndex2 = random.randint(0,len(aList) -1)
        if randomIndex not in resIndexList and randomIndex2 not in resIndexList:
            resIndexList.append(randomIndex)
            resIndexList.append(randomIndex2)
            tempVal1 = aList[randomIndex]
            tempVal2 = aList[randomIndex2]
            aList[randomIndex] = tempVal2
            aList[randomIndex2] = tempVal1
        else:
            while randomIndex in resIndexList or randomIndex2 in resIndexList or randomIndex == randomIndex2:
                randomIndex = random.randint(0,len(aList) -1)
                randomIndex2 = random.randint(0,len(aList) -1)
            resIndexList.append(randomIndex)
            resIndexList.append(randomIndex2)
            tempVal1 = aList[randomIndex]
            tempVal2 = aList[randomIndex2]
            aList[randomIndex] = tempVal2
            aList[randomIndex2] = tempVal1
            
                
    #print(aList)

    
    #print (almostIndex)



    
    #print(almostList)
    

    for i in range(5):
        startTime = time.perf_counter()
        #print(startTime)
        sortFunction(aList)
        endTime = time.perf_counter()
        #print(endTime)
        elapsedTime = endTime - startTime
        timeList.append(elapsedTime)
        
        

    avgTimeAlmost = sum(timeList) / 5
    avgTimeAlmostF = '{:f}'.format(avgTimeAlmost)

    
    #avgTimeCut = str(avgTime)[:8]
    
        
    aList.sort()
    return (avgTimeSortedF, avgTimeRandomF, avgTimeReverseF, avgTimeAlmostF)


########################################################


    

def main():

    myList10 = [i for i in range(10)]
    myList100 = [i for i in range(100)]
    myList1000 = [i for i in range(1000)]
    
#Key
#Grouped list index: x10 = 0, x100 = 1, x1000 = 2
#Individual tests index: Sorted = 0, Random = 1, Reverse = 2, Almost Sorted = 3

##########BubbleSort##############################
    
    bubble10 = testSort(bubbleSort, myList10)
    

    
    bubble100 = testSort(bubbleSort, myList100)
    
    #print(bubble100)

    bubble1000 = testSort(bubbleSort, myList1000)

    #print(bubble1000)

    bubbleTimes = [bubble10, bubble100, bubble1000]


    
##########BubbleSort##############################
##########SelectionSort###########################
    
    selection10 = testSort(selectionSort, myList10)
    

    #print(selection10)

    selection100 = testSort(selectionSort, myList100)

    #print(selection100)

    selection1000 = testSort(selectionSort, myList1000)

    #print(selection1000)

    selectionTimes = [selection10, selection100, selection1000]



##########SelectionSort###########################
##########InsertionSort###########################
    
    insertion10 = testSort(insertionSort, myList10)
    


    insertion100 = testSort(insertionSort, myList100)


    insertion1000 = testSort(insertionSort, myList1000)


    insertionTimes = [insertion10, insertion100, insertion1000]


    
##########InsertionSort###########################
##########ShellSort###############################
    

    
    shell10 = testSort(shellSort, myList10)
    


    shell100 = testSort(shellSort, myList100)


    shell1000 = testSort(shellSort, myList1000)


    shellTimes = [shell10, shell100, shell1000]



##########ShellSort###############################
##########MergeSort###############################

    merge10 = testSort(mergeSort, myList10)


    merge100 = testSort(mergeSort, myList100)


    merge1000 = testSort(mergeSort, myList1000)


    mergeTimes = [merge10, merge100, merge1000]



##########MergeSort###############################
##########QuickSort###############################

    quick10 = testSort(quickSort, myList10)


    quick100 = testSort(quickSort, myList100)


    quick1000 = testSort(quickSort, myList1000)


    quickTimes = [quick10, quick100, quick1000]


##########QuickSort###############################
##################################################

#_________BreakDown______________________________#

    inputType = ["Sorted", "Random", "Reverse", "Almost sorted"]
    

    for i in range (len(inputType)):

        print("Input type =", inputType[i])
        print('{:>28}'.format('avg time'), '{:>10}'.format('avg time'), '{:>10}'.format('avg time'))
        print('{:>16}'.format('Sort function'), '{:>10}'.format('(n=10)'), '{:>10}'.format('(n=100)'), '{:>11}'.format('(n=1000)'))
        print("-----------------------------------------------------")
        print('{:>16}'.format('bubbleSort'), '{:>11}'.format(bubbleTimes[0][i]), '{:>10}'.format(bubbleTimes[1][i]), '{:>10}'.format(bubbleTimes[2][i]))
        print('{:>16}'.format('selectionSort'), '{:>11}'.format(selectionTimes[0][i]), '{:>10}'.format(selectionTimes[1][i]), '{:>10}'.format(selectionTimes[2][i]))
        print('{:>16}'.format('insertionSort'), '{:>11}'.format(insertionTimes[0][i]), '{:>10}'.format(insertionTimes[1][i]), '{:>10}'.format(insertionTimes[2][i]))
        print('{:>16}'.format('shellSort'), '{:>11}'.format(shellTimes[0][i]), '{:>10}'.format(shellTimes[1][i]), '{:>10}'.format(shellTimes[2][i]))
        print('{:>16}'.format('mergeSort'), '{:>11}'.format(mergeTimes[0][i]), '{:>10}'.format(mergeTimes[1][i]), '{:>10}'.format(mergeTimes[2][i]))
        print('{:>16}'.format('quickSort'), '{:>11}'.format(quickTimes[0][i]), '{:>10}'.format(quickTimes[1][i]), '{:>10}'.format(quickTimes[2][i]))
        print()
        print()
                    

        

    

    
    
#Key
#Grouped list index: x10 = 0, x100 = 1, x1000 = 2
#Individual tests index: Sorted = 0, Random = 1, Reverse = 2, Almost Sorted = 3
main()



















