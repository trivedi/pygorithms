'''Count number of each character in a string and print
out the counts from highest to lowest.

Time: O(n) where n is the length of string
Space: O(n)
'''


def count_chars(s):
    freq = {}
    # Store frequency of each character
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    # Print counts from highest to lowest
    return sorted(freq.items(), key=lambda x: x[1], reverse=True)


print count_chars("hello")
