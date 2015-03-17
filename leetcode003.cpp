#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
using  namespace std;
const int maxn=1e5+10;
int visit[500];
int dp[maxn];
class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        int i, j;
        int last_start = 0;     // ��һ����Ӵ�����ʼλ��
        int maxlen =  0;
        dp[0] = 1;
        if(s.size()==1)return 1;
        if(s.size()==0)return 0;
        for(i = 1; i < s.size(); ++i)
        {
            for(j = i-1; j >= last_start; --j) // ��������һ����Ӵ���ʼλ��
            {
                if(arr[j] == arr[i])
                {
                    dp[i] = i - j;
                    last_start = j+1; // ����last_start
                    break;
                }
                else if(j == last_start)  // ���ظ�
                {
                    dp[i] = dp[i-1] + 1;
                }
            }
            if(dp[i] > maxlen)
            {
                maxlen = dp[i];
            }
        }
        return maxlen;
    }
};
