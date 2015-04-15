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
        if((x%10)==0 && (x/10)==0)/*这里也是要注意的一个点*/
        {
            return 0;
        }
        while (x>0)
        {
            int tsum = sum * 10 + (x % 10);
            if (tsum / 10 != sum)/*这里就是防止了溢出*/
                return 0;
            sum = tsum;
            x /= 10;
        }
        if (!isPosetive) sum *= -1;
        return sum;
    }
};
