""" Finds the max and min within a list """

def maxmin(list):
    min = list[0]
    max = list[0]
    length = len(list)
    for i in range(1,length):
        if list[i] > max:
            max = list[i]
        elif list[i] < min:
            min = list[i]
    print "The max is %s" % str(max)
    print "The min is %s" % str(min)
