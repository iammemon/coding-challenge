"""
problem : https://www.callicoder.com/minimum-difference-element-in-sorted-array/
pattern: floor and ceil of an element
 - do normal binary search
 - return the element if found
 - when search is completed compare the two pointers which has min diff and return it
"""


from typing import List

def findMin(nums:List[int],target:int)->int:
    left = 0
    right = len(nums) -1

    # edge case
    if target > nums[right]:
        return nums[right]
    elif target < nums[left]:
        return nums[left]

    while left<= right:
        mid = left + (right - left) //2
        if target == nums[mid]:
            return nums[mid]
        if target > nums[mid]:
            left = mid +1
        else:
            right = mid -1
    
    # both left and right will be the neighbour of the element such that floor and ceil
    if abs(nums[left] - target) < abs(nums[right] - target):
        return nums[left]
    else:
        return nums[right]

# nums= [2, 5, 10, 12, 15]
# print(findMin(nums,11))