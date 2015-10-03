#__author__ = 'tooweakchen'
#coding:utf-8
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack)<len(needle):
            #print "aaaa"
            return -1
        if haystack=="" and needle=="":
            return 0
        if haystack and not needle:
            return 0
        len1=len(haystack)
        len2=len(needle)
        for i in range(len1-len2+1):
            sum=0
            for j in range(len2):
                if haystack[i+j]!=needle[j]:
                    print haystack[i+j],needle[j]
                    break
                sum+=1
            if sum==len2:
                return i
        return -1
'''
solution=Solution()
str1="mississippi"
str2="issipi"
print solution.strStr(str1,str2)
'''
