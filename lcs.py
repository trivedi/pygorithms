'''
Longest Consecutive Sequence

Given an unsorted array find the length of the longest sequence.

[3, 2, 5, 4, 8, 10, 9, 100, 102, 101] -> 4  (2, 3, 4, 5)
'''


def lcs(nums):
    nums = set(nums)
    maxlen = 0
    while nums:
        first = last = nums.pop()

        # Keep decreasing value to find lower bound
        while first - 1 in nums:
            first -= 1
            nums.remove(first)

        # Keep increasing value to find upper bound
        while last + 1 in nums:
            last += 1
            nums.remove(last)

        # Check if we found a larger sequence
        maxlen = max(maxlen, last - first + 1)

    return maxlen


print lcs([3, 2, 5, 4, 8, 10, 9, 100, 102, 101])
