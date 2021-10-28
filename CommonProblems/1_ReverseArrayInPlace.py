# Interview Question #1

# The problem is that we want to reverse a T[] array in O(N)
# linear time complexity and we want the algorithm to be in-place as well!

# For example: input is [1,2,3,4,5] then the output is [5,4,3,2,1]


def reverse_arrays(inputArr):
    # Pointer to first item
    start_val_pointer = 0
    # Pointer to the last item
    end_val_pointer = len(inputArr)-1

    # While the end is greater than the start
    while end_val_pointer > start_val_pointer:
        # Swap values
        inputArr[start_val_pointer], inputArr[end_val_pointer] = inputArr[end_val_pointer], inputArr[start_val_pointer]
        # Increase start
        start_val_pointer = start_val_pointer + 1
        # Decrease end
        end_val_pointer = end_val_pointer - 1
    return inputArr

if __name__ == "__main__":

    inputArr = [1,2,3,4,5]

    print(reverse_arrays(inputArr))