#Uses python3

import sys

def largest_number(a):
    #separate numbers into nested arrays
    salary = ""
    b = []
    for i, x in enumerate(a):
        b.append([])
        xInt = int(x)
        if int(xInt) > 0:
            while xInt != 0:
                b[i].insert(0, xInt % 10)
                xInt = int((xInt-(xInt % 10))/10)
        else:
            b.insert(0, xInt)

    #find the number with the largest group of digits to append to the string
    nLen = []
    for n in b:
        nLen.append(len(n))

    curMaxIndexes = list(range(len(b)))
    i = 0
    while b:

        #loop through each in a copy of curMaxIndexes while updating curMaxIndexes
        curMaxIndexesOld = curMaxIndexes
        curMax = 0
        for nIndex in curMaxIndexesOld:
            n = b[nIndex]
            if n[i%nLen[nIndex]] > curMax:
                curMax = n[i%nLen[nIndex]]
                curMaxIndexes = [nIndex]
            elif n[i%nLen[nIndex]] == curMax:
                curMaxIndexes.append(nIndex)

        #if i is greater than all in curMaxIndexes then the two n are equivalent and can be added to salary in any order
        curMaxAllEqual = True
        for nIndex in curMaxIndexes:
            curMaxAllEqual = bool(curMaxAllEqual and nLen[nIndex] < i)
        
        
        if len(curMaxIndexes) == 1:
            curMaxIndex = curMaxIndexes[0]
            for digit in b[curMaxIndex]:
                salary += str(digit)
            del nLen[curMaxIndex]
            del b[curMaxIndex]
            curMaxIndexes = list(range(len(b)))
            i = 0
        elif curMaxAllEqual:
            for nIndex in reversed(curMaxIndexes):
                for digit in b[nIndex]:
                    salary += str(digit)
                del nLen[nIndex]
                del b[nIndex]
            curMaxIndexes = list(range(len(b)))
            i = 0
        else:
            i += 1

    return salary

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
