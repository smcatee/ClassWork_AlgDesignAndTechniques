# Uses python3
import sys

def optimal_summands(n):
    summands = []
    if n > 0:
        i = 1
        n = n - 1
        summands.append(i)
        while n > summands[-1]:
            i += 1
            summands.append(i)
            n = n - i
        summands[-1] += n
    
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
