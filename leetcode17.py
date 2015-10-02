#__author__ = 'tooweakchen'
#coding:utf-8
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        nums=[" ","1","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        list1=[]
        list2=[]
        if digits =="":
            return list1
        def dfs(cur):
            if cur >=len(digits):
                list1.append(''.join(list2))
            else:
                for x in nums[(int)(digits[cur]) - (int)('0')]:
                    list2.append(x)
                    dfs(cur+1)
                    list2.pop()
        dfs(0)
        return list1
'''
solution=Solution()
print solution.letterCombinations("")
'''