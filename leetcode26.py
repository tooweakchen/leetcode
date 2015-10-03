#__author__ = 'tooweakchen'
#coding:utf-8
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        sum=1
        item=nums[0]
        for num in nums:
            if num !=item:
                sum+=1
                item=num
        return sum
'''
solution=Solution()
list2=[1,1,2]
print solution.removeDuplicates(list2)
'''
