# Uses python3
import sys

# input is two lines, the first line is the sorted array (a), the second line is a list of keys (x)
# the first element of each line must be the length of the lines
# e.g.
#       5 1 4 6 9 12
#       3 6 1 8
# output: 2 0 -1

def binary_search(a, x):
    left, right = 0, len(a)
    output = -1
    while right > left:
        mid = int((right - left) / 2) + left
        if x == a[mid]:
            output = mid
            break
        elif x < a[mid]:
            right = mid
        else:
            left = mid + 1
    return output


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print (binary_search(a, x), end=" ")

