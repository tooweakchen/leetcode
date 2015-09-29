#__author__ = 'tooweakchen'
#coding:utf-8
import re
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p==s:
            return True
        else:
            flag=False
            for i in range(len(p)):
                if p[i]=='.' or p[i]=='*':
                    flag=True
                    break;
            if flag:
                item1=re.compile(p)
                item=re.match(item1,s)
                if item is not None:
                    if item.group()==s:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False

'''
aa=Solution()
str1=raw_input()
str2=raw_input()
aa.isMatch(str1,str2)
'''