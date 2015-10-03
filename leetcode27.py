#__author__ = 'tooweakchen'
#coding:utf-8
'''
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        list2=[]
        for i in range(len(nums)):
            if nums[i]!=val:
                list2.append(nums[i])
        return len(list2)
solution=Solution()
list1=[]
value=0
print solution.removeElement(list1,value)
'''


class Solution:
    def removeElement(self, nums, val):
        size=0
        length=len(nums)
        for i in range(length):
            if nums[i]!=val:
                nums[size]=nums[i]
                size+=1
        print size
'''
solution=Solution()
list1=[4,5]
value=4
solution.removeElement(list1,value)
'''