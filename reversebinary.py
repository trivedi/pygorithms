""" Solution to Spotify Tech Puzzle: reversebinary
    Reverses numbers in binary.
    i.e. Input: decimal
                    -> binary
                    -> reversed binary
         Output: -> decimal
    Author: Nishad Trivedi
            5/31/13
"""

import sys

def reversebinary(n):
    return int(bin(n)[2:][::-1],2)

def main():
    for number in sys.stdin:
        print reversebinary(int(number))

if __name__ == '__main__':
    main()


