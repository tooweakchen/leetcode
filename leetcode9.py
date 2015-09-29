#__author__ = 'tooweakchen'
#coding:utf-8
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str1=str(x)
        len1=len(str1)
        print len1
        for i in range(len1/2):
            if str1[i]!=str1[len1-1-i]:
                return False
                #break

        return True
'''
ceshi=Solution()
str2=raw_input()
num=int(str2)
ceshi.isPalindrome(num)
'''