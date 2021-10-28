def generalizedGCD(num, arr):
    # WRITE YOUR CODE HERE
    if arr == 0:
        return num
    else:
        return generalizedGCD(arr, num % arr)


