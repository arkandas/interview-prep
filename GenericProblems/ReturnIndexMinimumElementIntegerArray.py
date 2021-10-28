
# Return the index of the minimum element in an integer array

def findMinIndex(intArr):
    min_index = 0 # O(1)
    for i in range(len(intArr)): # n times
        if intArr[i] < intArr[min_index]: # O(1)
            min_index = i # O(1)
    return min_index


if __name__ == "__main__":

    testArray = [4, 3, 1, 78,61, 2]
    print(findMinIndex(testArray))
