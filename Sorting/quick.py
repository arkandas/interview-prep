# Quicksort is a divide and conquer algorithm.
# It first divides the input array into two smaller sub-arrays:
# the low elements and the high elements.
# It then recursively sorts the sub-arrays.
# The steps for in-place Quicksort are:
# 1. Pick an element, called a pivot, from the array.
# 2. Partitioning: reorder the array so that all elements with values less than the pivot come before the pivot,
# while all elements with values greater than the pivot come after it (equal values can go either way).
# After this partitioning, the pivot is in its final position. This is called the partition operation.
# 3. Recursively apply the above steps to the sub-array of elements with smaller values and separately to the sub-array of elements with greater values.

def quick_sort(nums,low,high):
    
	if low >= high:
		return
		
	pivot_index = partition(nums,low,high)
	quick_sort(nums,low, pivot_index-1)
	quick_sort(nums, pivot_index+1,high)
	
	
def partition(nums,low,high):

	pivot_index = (low+high)//2
	swap(nums,pivot_index,high)
	
	i = low
	
	for j in range(low,high,1):
		if nums[j] <= nums[high]:
			swap(nums,i,j)
			i = i + 1
			
	swap(nums,i,high)
	
	return i
	
def swap(nums,i,j):
	temp = nums[i]
	nums[i] = nums[j]
	nums[j] = temp
	
	
if __name__ == "__main__":
   
   nums = [-2,-1,0,1,0,-1,-2]
   quick_sort(nums,0,len(nums)-1)
   print(nums)
  