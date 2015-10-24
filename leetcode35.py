#__author__ = 'tooweakchen'
#coding:utf-8
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        flag=0
        for i in range(len(nums)):
            if nums[i]==target:
                flag=1
                return i
        if flag==0:
            flag1=0
            for i in range(len(nums)):
                if target<nums[i]:
                    flag1=1
                    return i
            if flag1==0:
                return len(nums)