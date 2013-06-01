""" Substring Pattern Matching - Brute Force implementation
    O(mn)
    Nishad Trivedi (4/11/13)
"""
def substring(text, pattern):
    n = len(text)
    m = len(pattern)
    for i in range(0,n-m):
        j = 0
        while (j < m and text[i+j] == pattern[j]):
            j = j + 1
        if (j == m):
            return True
    return False
