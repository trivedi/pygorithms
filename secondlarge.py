""" Finds the second largest element in a list """

def secondLarge(list):
    max = list[0]
    last_max = list[0]
    for num in list:
        if num > max:
            last_max = max
            max = num
    return last_max
