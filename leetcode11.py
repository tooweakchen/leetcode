#__author__ = 'tooweakchen'
#coding:utf-8
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea=0
        len1=len(height)
        left=0
        right=len1-1
        while(left<right):
            maxarea=max(maxarea,(right-left)*min(height[right],height[left]))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1

        return maxarea


'''
aa=Solution()
aa.maxArea([2,1])
'''