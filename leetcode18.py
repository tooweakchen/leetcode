#__author__ = 'tooweakchen'
#coding:utf-8
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums=sorted(nums)
        list1=[]
        len1=len(nums)
        for i in range(len1-3):
            num1=nums[i]
            for j in range(i+1,len1-2):
                num2=nums[j]
                l=j+1
                r=len1-1
                while(l<r):
                    sum=num1+num2+nums[l]+nums[r]
                    #print l,r
                    #print sum,num1,num2,nums[l],nums[r]
                    if sum ==target:
                        list2=[]
                        list2.append(num1)
                        list2.append(num2)
                        list2.append(nums[l])
                        list2.append(nums[r])
                        list2=sorted(list2)
                        if list2 not in list1:
                            list1.append(list2)
                        l+=1
                        r-=1
                    elif sum<target:
                        l+=1
                    elif sum>target:
                        r-=1

        return list1
'''
solution=Solution()
list3=[1,0,-1,0,-2,2]
print solution.fourSum(list3,0)
'''
