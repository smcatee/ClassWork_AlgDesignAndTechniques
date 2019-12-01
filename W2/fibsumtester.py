# Uses python3
import fibonacci_partial_sum
import fibonacci_partial_sum_fast
import numpy.random
import time

time_naive = 0
time_fast = 0
failures = 0

runs = 100
for i in range(1,runs):
    r = numpy.random.randint(1, high = 100000, size = 2)
    sfib = min(r)
    nfib = max(r)

    start_time_naive = time.time()
    ans_naive = fibonacci_partial_sum.fibonacci_partial_sum_naive(sfib,nfib)
    time_naive += time.time() - start_time_naive

    start_time_fast = time.time()
    ans_fast = fibonacci_partial_sum_fast.fibonacci_partial_sum_naive(sfib,nfib)
    time_fast += time.time() - start_time_fast


    print("\ns:", sfib, "\tn:", nfib, "\nNaive:",ans_naive,"\nFast:",ans_fast)
    
    if (ans_naive != ans_fast):
        failures += 1
        print("!-!-!-!-!-!-!-!-!-!-!--------FAILED-------!-!-!-!-!-!-!-!-!-!-!-!-!-!-!")


print("\n---Failures:" , failures, "\n")
print("Nieve took:", time_naive/runs, "\tFast took:", time_fast/runs)