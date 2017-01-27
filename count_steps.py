'''Count the number of different ways can you climb n stairs if
you can take only 1- or 2-step jumps?'''


def count_steps(n):
    if n <= 1:
        return 1
    else:
        return count_steps(n - 1) + count_steps(n - 2)


print count_steps(3)
print count_steps(4)
print count_steps(5)
