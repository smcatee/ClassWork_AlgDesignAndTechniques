# Uses python3
import sys
import time

def get_majority_element(a, left, right):
    time.sleep(0.5)
    print("\nget_majority_element")
    #print("left:", left, " right:", right)
    if left != right:
        mid = int((right-left)/2)+left #one problem is with this.
        
        a1 = get_majority_element(a, left, mid)
        if a1 == -1:
            return -1
        a2 = get_majority_element(a, mid+1, right)
        if a2 == -1:
            return -1
        
        aSorted = []
        equalCount = 0
        while a1 or a2:
            print("a1", a1)
            print("a2", a2)
            #take the last element of a1 and a2 if the exist
            a1FirstElem = int()
            a2FirstElem = int()
            if isinstance(a1, int):
                a1FirstElem, a1 = a1, False
            else:
                if a1:
                    a1FirstElem = a1.pop(0)
            if isinstance(a2, int):
                a2FirstElem, a2 = a2, False
            else:
                if a2:
                    a2FirstElem = a2.pop(0)

            if a1FirstElem and a2FirstElem:
                if a1FirstElem < a2FirstElem:
                    aSorted.append(a1FirstElem)
                    if len(aSorted) > 1:
                        equalCount = equalCount + 1 if aSorted[-1] == aSorted[-2] else 1
                elif a1FirstElem > a2FirstElem:
                    aSorted.append(a2FirstElem)
                    if len(aSorted) > 1:
                        equalCount = equalCount + 1 if aSorted[-1] == aSorted[-2] else 1
                else:
                    aSorted.append(a1FirstElem)
                    aSorted.append(a2FirstElem)
                    if len(aSorted) > 2:
                        equalCount = equalCount + 2 if aSorted[-2] == aSorted[-3] else 2
            elif a1FirstElem:
                aSorted.append(a1FirstElem)
                equalCount = equalCount + 1 if aSorted[-1] == aSorted[-2] else 1
            else:
                aSorted.append(a2FirstElem)
                equalCount = equalCount + 1 if aSorted[-1] == aSorted[-2] else 1
            print("equalCount", equalCount)
            if equalCount > nHalf:
                return -1
        print("aSorted", aSorted)
        return aSorted
    else:
        return a[left]


if __name__ == '__main__':
    input = sys.stdin.read() 
    n, *a = list(map(int, input.split()))
    nHalf = int(len(a)/2)
    if get_majority_element(a, 0, n-1) == -1:
        print(1)
    else:
        print(0)
