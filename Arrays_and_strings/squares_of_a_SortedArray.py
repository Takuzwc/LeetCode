# Given an integer array nums sorted in non-decreasing order, 
# return an array of the squares of each number sorted in non-decreasing order.

# Example
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Follow up: Squaring each element and sorting the new array is very trivial, 
# could you find an O(n) 
# solution using a different approach?

nums = [-4,-1,0,3,10]

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squared_array = []
        
        for i in range(len(nums)):
            squared_array.append(nums[i] ** 2)
            
        squared_array.sort()
        return squared_array