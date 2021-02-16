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

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newHead = None
        cur = head
        while cur != None:
            tmp = cur.next
            cur.next = newHead
            newHead = cur
            cur = tmp

        return newHead
