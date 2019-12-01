# Uses python3
import sys

def fibonacci_partial_sum_naive(s, n):
    m = 10
    #get rep for this modulo
    rep = [0, 1, 1]
    i = 2
    while ( [ rep[i-1], rep[i] ] != [0,1] ):
        rep.append( (rep[i-1] + rep[i]) % m )
        i += 1
    #trim the last two elements from rep
    del rep[-2:]

    #calculate the start and stop position and number of times a full loop is made
    ndig = (n+1)%len(rep)
    sdig = s%len(rep)
    loops = (n//len(rep) - s//len(rep)) - 1
    runningsum = 0
    if(loops == -1):
        runningsum = sum(rep[sdig:])
        if (ndig != 0):
            runningsum += sum(rep[:ndig])
            print(n,ndig)
    else:
        runningsum = sum(rep[sdig:]) + sum(rep[:ndig]) + loops*sum(rep)
    return runningsum%m

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))