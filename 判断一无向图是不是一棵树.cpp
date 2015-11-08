/*
    使用并查集
    1.只有一个根节点
    2.没有环

*/
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
using namespace std;
const int maxn=100000+10;
int fa[maxn],num[maxn];

int _find(int x)
{

    if(fa[x]!=x)
    {
        fa[x]=_find(fa[x]);
    }
    return fa[x];
}

bool Union(int a,int b)
{
    int faa=_find(a);
    int fab=_find(b);
    if(faa==fab)return false;
    if (faa!=fab)
    {
        if(num[faa]>num[fab])
        {
            fa[fab]=faa;
        }
        else
        {
            fa[faa]=fab;
            if(num[faa]==num[fab])
                num[fab]++;
        }
    }
    return true;
}

int main()
{

    int a,b;
    int k1,k2;
    int tcase=0;
    while(scanf("%d%d",&k1,&k2))
    {
        if(k1==-1&&k2==-1)
        {
            break;
        }
        map<int,int>mp;
        tcase++;
        for(int i=1; i<maxn; i++)
        {
            fa[i]=i;
            num[i]=0;
        }
        bool flag=true;
        while(!(k1==k2&&k1==0))
        {
            mp[k1]=1;
            mp[k2]=1;
            if(!Union(k1,k2))flag=false;
            scanf("%d%d",&k1,&k2);
        }
        int sum=0;
        for(int i=1; i<maxn; i++)
        {
            if(mp[i]==1&&fa[i]==i)
            {
                sum++;
            }
        }
        if(sum>1)
        {
            flag=false;
        }
        /*
        if(flag)
        {
            cout<<"这是一棵树!!"<<endl;
        }
        else
        {
            cout<<"这不是一颗树!!"<<endl;
        }
        */
        if(flag)cout<<"Yes"<<endl;
        else cout<<"No"<<endl;
    }
    return 0;
}
