# Uses python3
import sys

def gcd( a, b ):
    r = min( a, b )
    while ( a%r != 0 or b%r != 0 ):
        r = max( a%r, b%r )

    return a * b / r

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map( int, input.split() )
    print(gcd( a, b ))