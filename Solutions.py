#!/usr/bin/python
class Solution(object):
    def sortedSquares(self, nums):
         return sorted(x*x for x in nums)
         
    def sortedSquares2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            nums[i] = nums[i]*nums[i]

        nums.sort()
        return nums
