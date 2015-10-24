#__author__ = 'tooweakchen'
#coding:utf-8
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list1=[]
        if len(nums)==1:
            if nums[0]==target:
                list1.append(0)
                list1.append(0)
        else:
            nums=sorted(nums)
            flag=1
            beginpos=-1
            for i in range(len(nums)):
                if nums[i]==target and flag==1:
                    beginpos=i
                    list1.append(beginpos)
                    flag=0
                elif nums[i]==target:
                    if i==len(nums)-1:
                        endpos=i
                        list1.append(endpos)
                    elif nums[i+1]!=target:
                        endpos=i
                        list1.append(endpos)
            if len(list1)==1:
                list1.append(beginpos)
        if len(list1)==0:
            list1.append(-1)
            list1.append(-1)
        return list1

