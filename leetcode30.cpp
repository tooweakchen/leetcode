#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

class Solution
{
public:
    vector<int> findSubstring(string s, vector<string>& words)
    {
        vector<int>v;
        if(s.size()==0||words.size()==0)return v;
        map<string,int>m1;
        for(int i=0; i< words.size(); i++)
        {
            m1[words[i]]++;
        }
        int len2=words[0].size();
        map<string,int>m2;
        for(int i=0; i+len2* words.size()<=s.size(); i++)
        {
            m2.clear();
            map<string,int>::iterator it;
            int k,j;
            for(j=i,k=0; k< words.size(); k++,j+=len2)
            {
                string s1=s.substr(j,len2);
                it=m1.find(s1);
                if(it==m1.end())
                {
                    break;
                }
                m2[s1]++;
                if (m2[s1]>m1[s1])break;
            }
            if(k== words.size())
            {
                v.push_back(i);
            }
        }
        return v;
    }
};
