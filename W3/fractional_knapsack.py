# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    
  	#find the order of value/weight
   
    rowsums = [0] * len(weights)
    lootOrder = [0] * len(weights)
   
    for i, v in enumerate(values):
        if(len(weights) == 1):
            lootOrder[i] = 1
            break
        for j, w in enumerate(weights):
            if i < j:
                if ( v * w > values[j] * weights[i] ):
                    rowsums[i] += 1
                elif ( v * w == values[j] * weights[i] ):
                    rowsums[i] += 1
                    rowsums[j] += 1
                elif ( v * w < values[j] * weights[i] ):
                    rowsums[j] += 1
        lootOrder[i] = len(rowsums) - rowsums[i]

            
    #add loot to bag
    lootValue = 0
    lootWeight = 0
    currentLoot = 1
    
    while ( lootWeight <= capacity and currentLoot <= len(lootOrder) ):
        if currentLoot in lootOrder:
            lootIndex = lootOrder.index(currentLoot)
       	    if (weights[lootIndex] + lootWeight) > capacity:
                proportion = (capacity - lootWeight)/weights[lootIndex]
                lootWeight += proportion * weights[lootIndex]
                lootValue += proportion * values[lootIndex]
                break
            else:
                lootValue += values.pop(lootIndex)
                lootWeight += weights.pop(lootIndex)
                del lootOrder[lootIndex]
        else:
            currentLoot += 1
    
    return lootValue


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
