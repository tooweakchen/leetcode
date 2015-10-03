#__author__ = 'tooweakchen'
#coding:utf-8
class Solution:
    def isValid(self,s):
        """
        :type s: str
        :rtype: bool
        """
        flag=True
        str11="()"
        str22="[]"
        str33="{}"
        stack=[]
        if s=='[' or s==']' or s=='(' or s==')' or s=='{' or s=='}':
            return False
        for str1 in s:
            if str1=='(' or str1=='[' or str1=='{':
                stack.append(str1)
            else:
                str3=""
                if len(stack):
                    str2=stack.pop()
                    str3=str2+str1
                    if str1==')':
                        if str3==str11:
                            #print "bbbbbbbbb"
                            continue
                        else:
                            return False
                            #print False
                            #break
                    elif str1==']':
                        if str3==str22:
                            #print "ccccccccc"
                            continue
                        else:
                            return False
                            #print False
                            #break
                    elif str1=='}':
                        if str3==str33:
                            #print "aaaaaaaaa"
                            continue
                        else:
                            return False
                            #print False
                            #break
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False
'''
solution=Solution()
s="()(]{}"
solution.isValid(s)
'''


