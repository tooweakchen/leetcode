#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
using namespace std;
class Solution
{
public:
    string convert(string s, int nRows)
    {
        int len=s.size();
        int i=0,j;
        vector<string>a(nRows);
        while(i<len)
        {
            for(j=0; j<nRows&&i<len; j++,i++)a[j]+=s[i];
            for(j=nRows-2; j>0&&i<len; j--,i++)a[j]+=s[i];

        }
        string res;
        for(i=0; i<nRows; i++)
        {
            for(int j=0; j<a[i].size(); j++)
            {
                res+=a[i][j];
            }

        }
        return res;
    }
};
