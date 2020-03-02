# Uses python3
import sys
import random

def partition3(a, l, r):
    #write your code here
    pass

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a):
    print(a)
    print(a[0])
    sortedList = list(a[0])
    smallerList = list()
    largerList = list()

    for i in range(1, len(a) -1):
        if a[0] == a[i]:
            sortedList += list(a[i])
        elif a[0] > a[i]:
            smallerList += list(a[i])
        else:
            largerList += list(a[i])
    
    if largerList:
        sortedList = sortedList + randomized_quick_sort(largerList)
    if smallerList:
        sortedList = randomized_quick_sort(smallerList) + sortedList
    
    return sortedList
    

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    a = randomized_quick_sort(a)
    print(a)
    for x in a:
        print(x, end=' ')
