#__author__ = 'tooweakchen'
#coding:utf-8

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        flag=True
        nums=sorted(nums)
        len1=len(nums)
        for i in range(len1):
            j=i+1
            k=len1-1
            while j<k:
                sum=nums[i]+nums[j]+nums[k]
                if flag:
                    minsum=sum
                    flag=False
                else:
                    if(abs(sum-target)<abs(minsum-target)):
                        minsum=sum

                if minsum==target:
                    return minsum
                if sum>target:
                    k-=1
                else:
                    j+=1

        return minsum


'''
solution=Solution()
list1=[-1,2,1,-4]
item=1
print solution.threeSumClosest(list1,1)
'''