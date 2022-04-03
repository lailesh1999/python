
def bubble_sort(b):
    for i in range (0,len(b)):
        for j in range(0,len(b)-i-1):
            if b[j] < b[j+1]:
                temp = b[j]
                b[j] = b[j+1]
                b[j+1] = temp
    return b



