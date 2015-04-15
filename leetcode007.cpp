#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;
class Solution
{
public:
    int reverse(int x)
    {
        int sum = 0;
        bool isPosetive = true;
        if (x<0)
        {
            isPosetive = false;
            x =abs(x);
        }
        if((x%10)==0 && (x/10)==0)/*����Ҳ��Ҫע���һ����*/
        {
            return 0;
        }
        while (x>0)
        {
            int tsum = sum * 10 + (x % 10);
            if (tsum / 10 != sum)/*������Ƿ�ֹ�����*/
                return 0;
            sum = tsum;
            x /= 10;
        }
        if (!isPosetive) sum *= -1;
        return sum;
    }
};
