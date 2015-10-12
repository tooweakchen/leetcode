#__author__ = 'tooweakchen'
#coding:utf-8
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        str="1"
        for i in range(1,n):
            str1=str
            str=""
            sum=1
            for j in range(1,len(str1)):
                if str1[j]==str1[j-1]:
                    sum+=1
                elif str1[j]!=str1[j-1]:
                    str+=("%d"%sum+str1[j-1])
                    sum=1
            str+=("%d"%sum+str1[len(str1)-1])

        return str
'''
solution=Solution()
n=4
solution.countAndSay(n)
'''