#__author__ = 'tooweakchen'
#coding:utf-8
#这是我觉得应该是正确的
#因为case中竟然把+-2输出０，而我觉得应该是－2，下面这种就可以输出来
import re
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX=2147483647
        INT_MIN=-2147483648
        str=str.strip()
        if str:
            item1=re.findall(r'\-\d+',str)
            item2=re.findall(r'\+\d+',str)
            if len(item1)!=0:
                item=item1[0]
            elif len(item2)!=0:
                item=item2[0]
            else:
                item2=re.match(r'[+-]?\d+',str)
                if item2 is not None:
                    item=item2.group()
        else:
            return 0
        try:
            item=int(item)
            if item>INT_MAX:
                return INT_MAX
            elif item<INT_MIN:
                return INT_MIN
            else:
                return item
        except:
            return 0

s=Solution()
k=s.myAtoi("++++++++++++++2145asdfs15afkjbsdj")
print k

#这种是AC过去的。

import re

class Solution:
    def myAtoi(self, str):
        str = str.strip()
        if str:#这里要考虑""这种情况
            str = re.match(r'^[+-]?\d+', str)
            if str is not None:
                str=str.group()
            else:
                return 0
            MAX_INT = 2147483647
            MIN_INT = -2147483648

            try:
                ret = int(str)
                if ret > MAX_INT:
                    return MAX_INT
                elif ret < MIN_INT:
                    return MIN_INT
                else:
                    return ret
            except:
                return 0
        else:
            return 0

s=Solution()
k=s.myAtoi("-2222fdgaf")
print k