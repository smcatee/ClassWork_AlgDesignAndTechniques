# Uses python3
def calc_fib(n):
    fib1 = 0
    fib2 = 1
    for x in range(0, n):
        if (x%2):
            fib2 += fib1
        else:
            fib1 += fib2
    return fib2 if (n%2) else fib1

n = int(input())
print(calc_fib(n))
