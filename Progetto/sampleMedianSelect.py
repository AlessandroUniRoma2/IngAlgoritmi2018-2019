"""
Francesco Cavaliere, 0253942
Alessandro Cavaliere, 0253983

"""

from __init__ import printSwitch
import random
import sys
sys.setrecursionlimit(1000000000)



def newQuickSort(a, det=True):
    recursiveQuickSort(a, 0, len(a) - 1, det)


def recursiveQuickSort(a, left, right, det=True):
    if left >= right:
        return
    if printSwitch.dumpOperations:
        print("recursiveQuickSort({},{})".format(left, right))

    mid = partition(a, left, right)
    recursiveQuickSort(a, left, mid - 1, det)
    recursiveQuickSort(a, mid + 1, right, det)


def partition(a, left, right):
    mid = sampleMedianSelect(a)
    inf = left
    sup = right + 1
    if inf < mid < sup:
        a[left], a[mid] = a[mid], a[left]
    else:
        if printSwitch.dumpOperations:
            print("Cerco un altro mediano...\n")

        sampleMedianSelect(a)

    mid = left  # the median is the first elem of the array
    while True:
        inf += 1

        while inf <= right and a[inf] <= a[mid]:
            inf += 1

        sup -= 1

        while a[sup] > a[mid]:
            sup -= 1

        if inf < sup:

            a[inf], a[sup] = a[sup], a[inf]
        else:
            break

    a[mid], a[sup] = a[sup], a[mid]
    if printSwitch.dumpOperations:
        print("- " * left + str(a[left:right + 1]) + " -" * (len(a) - right - 1), "\n")
    return sup


def sampleMedianSelect(a):
    """ Genera casualmente un sottoinsieme V di k elementi a partire dall'array A, ne seleziona il mediano e lo
    utilizza come pivot.
    """
    v = random.sample(a, 5)
    if printSwitch.dumpOperations:
        print("Array random :", v, )
    m = v[(len(v)//2)]
    if printSwitch.dumpOperations:
            print("Il mediano selezionato è: ", m, "")
    mid = a.index(m)
    return mid


if __name__ == "__main__":
    a = [4, 1234, 34, 566, 8, 2, 5346, 8, 3, 263, 7, 8, 3, 7, 57, 2, 43, 87, 845, 42]
    print("ARRAY DI PARTENZA:", a, "\n")
    newQuickSort(a)
    print("ARRAY FINALE:", a)