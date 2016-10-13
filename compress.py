'''
Basic in-place string compression

compress("aabbbbccc") -> "a3b4c3"
'''
import ctypes  # normal strings are not mutable in Python


def compress(string):
    prev = string[0]
    start = 0
    count = 1
    for i in range(0, len(string)):
        if (prev == string[i]):
            count += 1
        else:
            count = str(count)
            string[start] = prev
            string[start + 1] = count
            prev = string[i]
            start = start + len(count) + 1
            count = 1
    print start
    return string[0:start]


string = ctypes.create_string_buffer("aabbbbccc")
print compress(string)
