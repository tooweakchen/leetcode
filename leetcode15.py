#__author__ = 'tooweakchen'
#coding:utf-8
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums=sorted(nums)
        list2=[]
        len1=len(nums)
        for i in range(len1):
            while(i > 0 and i < len1 and nums[i] == nums[i-1]):
                 i+=1
            j=i+1
            k=len1-1
            while j<k :
                list3=[]
                #print nums[j],nums[k],nums[i]
                sum=nums[j]+nums[k]+nums[i]
                #print sum
                if sum==0:
                    list3.append(nums[i])
                    list3.append(nums[j])
                    list3.append(nums[k])
                    if list3 not in list2:
                        list2.append(list3)
                    j+=1
                    k-=1
                    while(j < k and nums[j] == nums[j-1]):
                        j+=1
                    while(k > j and nums[k] == nums[k+1]):
                        k-=1
                elif sum<0:
                    j+=1
                    while(j < k and nums[j] == nums[j-1]):
                        j+=1
                elif sum>0:
                    k-=1
                    while(k > j and nums[k] == nums[k+1]):
                        k-=1

        #print list2
        return list2

'''
solution=Solution()
list1=[-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
print solution.threeSum(list1)
'''