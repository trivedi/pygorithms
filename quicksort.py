'''
Quicksort

In-place sorting

Best Case: O(nlgn) w/ O(lgn) auxillary space on stack
Average Case: O(nlgn)
Worst Case: O(n^2) w/ O(n) auxillary space on stack

10/22/13 at 12:13 am
'''

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

# Helper function
def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i] # Swap
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def test():
    A = [5, 3, 6, 2, 7, 10, 11, 2, 1]
    quicksort(A, 0, len(A)-1)
    print A

if __name__ == "__main__":
    test()
