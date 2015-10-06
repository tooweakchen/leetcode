#__author__ = 'tooweakchen'
#coding:utf-8
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        list1=[]
        list1=str.split(' ')
        if len(pattern)!=len(list1):
            return False
        d=dict()
        for i in range(len(pattern)):
            if pattern[i] in d:
                str1=d[pattern[i]]
                if str1!=list1[i]:
                    return False
            else:
                d[pattern[i]]=list1[i]
        list2=d.keys()
        for i in range(len(list2)):
            for j in range(len(list2)):
                if i!=j:
                    if d[list2[j]]==d[list2[i]]:
                        return False

        #print list2
        return True
'''
solution=Solution()
str2="abba"
str3="dog cat cat fish"
print solution.wordPattern(str2,str3)
'''