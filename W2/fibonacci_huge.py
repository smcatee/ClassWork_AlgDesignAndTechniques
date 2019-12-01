# Uses python3
import sys

def get_fibonacci_huge(n, m):
    #get rep for this modulo
    rep = [0, 1, 1]
    i = 2
    while ( [ rep[i-1], rep[i] ] != [0,1] ):
        rep.append( (rep[i-1] + rep[i]) % m )
        i += 1
    #trim the last two elements from rep
    del rep[-2:]

    #using n%len(rep) as index, return fib number
    return rep[n%len(rep)]


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
