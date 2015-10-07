#__author__ = 'tooweakchen'
#coding:utf-8
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        list2=[]
        flag=False
        len1=len(nums)
        if len1>=2:
            global pos,pos1
            for i in range(len1-2,-1,-1):
                if nums[i]<nums[i+1]:
                    pos=i
                    flag=True
                    break
            if not flag:
                for i in range(len1-1,-1,-1):
                    list2.append(nums[i])
                for i in range(len1):
                    nums[i]=list2[i]

            for i in range(len1-1,pos,-1):
                if nums[i]>nums[pos]:
                    pos1=i
                    nums[pos1],nums[pos]=nums[pos],nums[pos1]
                    break
            for i in range(0,pos+1,1):
                list2.append(nums[i])
            for i in range(len1-1,pos,-1):
                list2.append(nums[i])
            for i in range(len1):
                nums[i]=list2[i]


'''
设有排列(p)=2763541，按照字典式排序，它的下一个排列是什么？
1.2763541 （找最后一个正序35）
2.2763541 （找3后面比3大的最后一个数4）
3.2764531 （交换3,4的位置）
4.2764135 （把4后面的5,3,1反转）
'''
