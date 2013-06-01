def insertionSort(list):
    for i in range(1, len(list)):   # start at 1st element, not zeroeth
        current = list[i]
        prev = list[i-1]
        if current < prev:
            list[i] = prev          # swap prev and current
            list[i-1] = current
    return list
        
        