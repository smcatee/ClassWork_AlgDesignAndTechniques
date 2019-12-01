# Uses python3
import sys

def get_change(m):
    
    #1 5 10
    n = 0
   	
    if ((m//5)%2) == 1:
        n += 1
    n += (m//10) + (m%5)
    
    
    return n

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
