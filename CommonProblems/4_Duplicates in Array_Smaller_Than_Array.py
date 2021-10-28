
# ONLY WHERE THE LENGTH OF THE INTEGERS IS SMALLER THAN THE LENGTH OF THE ARRAY
# Consider all the items of array T[]:

# Check the sign of T[abs(T[i])]:
#    if it is positive:
#        flip the sign -> T[abs(T[i])] = - T[abs(T[i])]
#    else:
#       the given i item is a repetition

def duplicates(nums):

    for num in nums:
        if nums[abs(num)] >= 0:
            nums[abs(num)] = -nums[abs(num)]
        else:
            print('DUPLICATE FOUND!: ', abs(num))

if __name__ == "__main__":

    nums = [2, 6, 5, 4, 4, 3, 2, 7]
    duplicates(nums)