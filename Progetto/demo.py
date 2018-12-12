# coding: utf-8

from time import time
import random
from __init__ import printSwitch
import sampleMedianSelect
from strutture import Sorting
from strutture import HeapMax


def sortingTest(inputList, sortingFunction, secondPar=None, thirdPar=None):
    l = list(inputList)  # copy the list. Equivalent to l=input[:].
    start = time()
    if secondPar != None and thirdPar != None:
        sortingFunction(l, secondPar, thirdPar)
    elif secondPar != None:
        sortingFunction(l, secondPar)
    else:
        sortingFunction(l)

    return time() - start

def sortPython(inputList):
    start = time()
    inputList.sort()
    return time() - start


if __name__ == "__main__":
    # Inizializzazione
    inputType = 0  # 1 crescente, -1 decrescente, 0 random
    steps = 5000
    slowAlgorithms = False

    inputList = [None] * steps
    for i in range(0, steps):
        if inputType == 1:
            inputList[i] = i
        elif inputType == -1:
            inputList[i] = steps - i
        elif inputType == 0:
            inputList[i] = random.randint(0, steps)
        else:
            raise Exception("You used an invalid inputType parameter!")
    printSwitch.dumpOperations = False

    if slowAlgorithms:
        runningTime = sortingTest(inputList, Sorting.selectionSort)
        print("selectionSort required {} seconds.".format(runningTime))
        runningTime = sortingTest(inputList, Sorting.insertionSortUp)
        print("insertionSortUp required {} seconds.".format(runningTime))
        runningTime = sortingTest(inputList, Sorting.insertionSortDown)
        print("insertionSortDown required {} seconds.".format(runningTime))
        runningTime = sortingTest(inputList, Sorting.bubbleSort)
        print("bubbleSort required {} seconds.".format(runningTime))

        print('\n')
    runningTime = sortingTest(inputList, sampleMedianSelect.newQuickSort, True)
    print("newQuickSort required {} seconds.".format(runningTime))
    runningTime = sortingTest(inputList, Sorting.quickSortIter, True)
    print("quickSortIter-Det required {} seconds.".format(runningTime))
    runningTime = sortingTest(inputList, Sorting.quickSortIter)
    print("quickSortIter-NonDet required {} seconds.".format(runningTime))
    runningTime = sortingTest(inputList, Sorting.quickSort, True)
    print("quickSort(Rec)-Det required {} seconds.".format(runningTime))
    runningTime = sortingTest(inputList, Sorting.quickSort)
    print("quickSort(Rec)-NonDet required {} seconds.".format(runningTime))
    print('')
    runningTime = sortingTest(inputList, Sorting.mergeSort)
    print("mergeSort required {} seconds.".format(runningTime))
    print('')
    runningTime = sortingTest(inputList, Sorting.heapSort)
    print("heapSort required {} seconds.".format(runningTime))
    print("sort() required {} seconds.".format(sortPython(inputList)))


    b = 400
    runningTime = sortingTest(inputList, Sorting.radixSort, steps, b)
    print("radixSort({},{}) required {} seconds.".format(steps, b, runningTime))
    b = 100
    runningTime = sortingTest(inputList, Sorting.radixSort, steps, b)
    print("radixSort({},{}) required {} seconds.".format(steps, b, runningTime))
    b = 10
    runningTime = sortingTest(inputList, Sorting.radixSort, steps, b)
    print("radixSort({},{}) required {} seconds.".format(steps, b, runningTime))
    b = 2
    runningTime = sortingTest(inputList, Sorting.radixSort, steps, b)
    print("radixSort({},{}) required {} seconds.".format(steps, b, runningTime))



