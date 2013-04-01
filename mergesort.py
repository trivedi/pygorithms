def mergesort(list):
    """Merge Sort with complexity O(nlogn
       Usage: >>> mergesort([1,5,2,8,3,8,2,7,4])
              [1,2,2,3,4,5,7,8,8]
    """
    mid = len(list)/2
    left = list[:mid]
    right = list[mid:]

    # Keep halving both sides until there are single-element lists
    if len(left) > 1:
        left = mergesort(left)

    if len(right) > 1:
        right = mergesort(right)

    # Create a new list that's sorted
    newlist = []
    while left and right:
        if left[-1] >= right[-1]:
            newlist.append(left.pop())
        else:
            newlist.append(right.pop())
    newlist.reverse()
    return (left or right) + newlist
