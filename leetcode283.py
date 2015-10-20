#__author__ = 'tooweakchen'
#coding:utf-8
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        len1=len(nums)
        num1=0

        for i in range(len1):
            if nums[i]!=0:
                nums[num1]=nums[i]
                num1+=1
        len1-=num1
        for i in range(len1):
            nums[num1]=0
            num1+=1
        #return nums
'''
solution=Solution()
nums=[0,1,0]
print solution.moveZeroes(nums)
'''

