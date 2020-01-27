# O(log(n)) time O(1) space

def binarySearch(array, target):
    return bsHelper(array, target, 0, len(array) - 1)

def bsHelper(array, target, left, right):
	while left <= right:
		mid = (left + right) // 2
		potentialMatch = array[mid]
		if potentialMatch == target:
			return mid
		elif potentialMatch > target:
			right = mid - 1
		elif potentialMatch < target:
			left = mid + 1
	return -1
	