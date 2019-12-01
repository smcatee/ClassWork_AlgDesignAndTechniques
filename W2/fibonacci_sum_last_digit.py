# Uses python3
import sys

def get_fibonacci_huge(n):
    m = 10
    #get rep for this modulo
    rep = [0, 1, 1]
    fsum = [0, 1, 2]
    i = 2
    while ( [ rep[i-1], rep[i] ] != [0,1] ):
        rep.append( (rep[i-1] + rep[i]) % m )
        fsum.append( fsum[i] + rep[i+1] )
        i += 1
    #trim the last two elements from rep
    del rep[-2:]
    del fsum[-2:]

    #using n%len(rep) as index, return fib number
    return ( (fsum[-1] * (n//len(rep))) + fsum[n%len(rep)] )%m


if __name__ == '__main__':
    input = sys.stdin.read()
    #n, m = map(int, input.split())
    n = int(input)
    print(get_fibonacci_huge(n))
