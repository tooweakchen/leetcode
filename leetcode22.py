#__author__ = 'tooweakchen'
#coding:utf-8
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        list1=[]
        def work(step,maxstep,leftnum,lefttotalnum,s):
            if lefttotalnum*2>maxstep:
                return
            if step==maxstep:
                list1.append(s)
                return
            for i in range(2):
                if i==0:
                    work(step+1,maxstep,leftnum+1,lefttotalnum+1,s+'(')
                else:
                    if leftnum>0:
                        work(step+1,maxstep,leftnum-1,lefttotalnum,s+')')

        work(0,2*n,0,0,"")
        return list1

'''
solution=Solution()
print solution.generateParenthesis(3)
'''