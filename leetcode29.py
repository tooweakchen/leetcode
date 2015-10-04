#__author__ = 'tooweakchen'
#coding:utf-8
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if (dividend==-divisor) or (-dividend==divisor):
            return -1
        if dividend==divisor:
            return 1
        flag=True
        if dividend<0 and divisor>0:
            flag=False
        elif dividend >0 and divisor <0:
            flag=False
        sum=0
        num1=abs(dividend)
        num2=abs(divisor)
        while num1>=num2:
            num3=num2
            ant=0
            while num1>=num3:
                num1-=num3
                sum+=(1<<ant)
                ant+=1
                num3<<=1
        MIN=-2147483648
        MAX=2147483647
        if flag==False:
            sum=-sum
        max1=max(sum,MIN)
        min1=min(max1,MAX)
        return min1
'''
solution=Solution()
num11=16
num22=3
print solution.divide(16,3)
'''

