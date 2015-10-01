#__author__ = 'tooweakchen'
#coding:utf-8
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        #返回list中最小的值
        s1 = min(strs)
        #返回list中最大的值
        s2 = max(strs)
        #enumerate函数用于遍历序列中的元素以及它们的下标
        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]
        return s1

solution=Solution()
print solution.longestCommonPrefix(['aa','abhbh','a'])