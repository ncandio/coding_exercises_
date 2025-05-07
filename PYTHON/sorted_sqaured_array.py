def sortedSquaredArray(array):
    return sorted([array[i]*array[i] for i in range(0,len(array))])