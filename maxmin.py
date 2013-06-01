def maxmin(list):
    min = list[0]
    max = list[0]
    length = len(list)
    for i in range(1,length):
        if list[i] > max:
            max = list[i]
        elif list[i] < min:
            min = list[i]
    print "The max is "+str(max)
    print "The min is "+str(min)
