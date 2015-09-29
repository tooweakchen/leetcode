#__author__ = 'tooweakchen'
#coding:utf-8
'''
def numToRomanNum(Num):
    """digital will be converted into Roman numerals,Ex: numToRomanNum(3999)"""
    if Num < 1 or Num > 3999:
         print 'The Num must in 1-3999'
    else:
         NumDic = {
             '1':('I','IV','V','IX'),
             '2':('X','XL','L','XC'),
             '3':('C','CD','D','CM'),
             '4':('M')
             }
         items = sorted(NumDic.items())
         retstr = ''
         for item in items:
             str = ''
             (Num,modNum) = divmod(Num,10)
             if modNum != 0:
                 if item[0] != '4':
                     if modNum <= 3:
                         while modNum > 0:
                             str = str.join(['',item[1][0]])
                             modNum -= 1
                     elif modNum < 5:
                         str = item[1][1]
                     elif modNum == 5:
                         str = item[1][2]
                     elif modNum < 9:
                         str = item[1][2]
                         while modNum > 5:
                             str = str.join(['',item[1][0]])
                             modNum -= 1
                     else:
                         str = item[1][3]
                 else:
                     while modNum > 0:
                         str = str.join(['',item[1][0]])
                         modNum -= 1
                 retstr = str.join(['',retstr])
         return retstr

k=numToRomanNum(121)
print k
'''

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        gewei=['I','II','III','IV','V','VI','VII','VIII','IX']
        shiwei=['X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
        baiwei=['C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
        qianwei=['M','MM','MMM']
        geweishu=num%10
        #print geweishu
        shiweishu=num/10%10
        #print shiweishu
        baiweishu=num/100%10
        #print baiweishu
        qianweishu=num/1000
        #print qianweishu
        str="";
        if qianweishu:
            str+=qianwei[qianweishu-1]
        #print str
        if baiweishu:
            str+=baiwei[baiweishu-1]
        #print str
        if shiweishu:
            str+=shiwei[shiweishu-1]
        #print str
        if geweishu:
            str+=gewei[geweishu-1]
        #print str
        return str

'''
aa=Solution()
aa.intToRoman(121)
'''