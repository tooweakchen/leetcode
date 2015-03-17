/*
 最长不重复子串
 方法一：
 直接O（n2），很暴力

 方法二：
 最坏的情况是O（n2）
 有点DP的影子。
*/
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
using namespace std;
const int maxn=1e5+10;
int dp[maxn];
int visit[500];
string s;

void work()
{
    memset(visit,0,sizeof(visit));
    int i,j;
    int max1=0;
    s="aaaa";
    int len=s.size();
    if(len==0)cout<<0<<endl;
    if(len==1)cout<<1<<endl;

    for( i=0; i<len; i++)
    {
        memset(visit,0,sizeof(visit));
        visit[s[i]]=1;
        for( j=i+1; j<len; j++)
        {
            if(visit[s[j]]==0)
            {
                visit[s[j]]=1;
            }
            else
            {
                if(j-i>max1)
                {
                    max1=j-i;

                }
                break;
            }
        }
        if(j==len&&(j-i)>max1)
        {
            max1=j-i;
        }
    }

    cout<<max1<<endl;
}

void work1()
{
    s="aaaa";
    int len=s.size();
    if(len==0)cout<<0<<endl;
    if(len==1)cout<<1<<endl;
    int i,j;
    int last_weizhi=0;
    memset(dp,0,sizeof(dp));
    dp[0]=1;
    int max1=0;

    for(int i=1; i<len; i++)
    {
        for(int j=i-1; j>=last_weizhi; j--)
        {
            if(s[j]==s[i])
            {
                dp[i]=i-j;
                last_weizhi=j+1;
                break;
            }
            else if(j==last_weizhi)
            {
                dp[i]=dp[i-1]+1;
            }
        }
        if(dp[i]>max1)
        {
            max1=dp[i];
        }
    }
    cout<<max1<<endl;

}

int main()
{
    work();
    work1();
}
