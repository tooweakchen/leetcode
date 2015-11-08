/**
  判断有向图是不是一颗树。
  1.只有一个根节点
  2.每个结点的入度数不能大于1
  3.不能有环
*/

#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
using namespace std;
const int maxn=100+10;
int dis[maxn][maxn],vis[maxn];
int in[maxn];
int fa[maxn];
int n;

int find(int x)
{
    while(x!=fa[x])
    {
        x=fa[x];
    }
    return x;
}

bool Union(int a,int b)
{
    in[b]+=1;
    int x=find(a);
    int y=find(b);
    if(x==y)return false;
    fa[y]=x;
    return true;
}

int main()
{
    while(scanf("%d",&n)!=EOF)
    {
        for(int i=0; i<maxn; i++){
            in[i]=0;
            fa[i]=i;
        }
        if(n==0)break;
        int a,b;
        map<int,int>mp;
        mp.clear();
        bool flag=true;
        for(int i=0; i<n; i++)
        {
            scanf("%d%d",&a,&b);
            mp[a]=1;
            mp[b]=1;
            if(!Union(a,b))flag=false;
        }
        int sum=0;
        for(int i=0; i<maxn; i++)
        {
            if(mp[i]&&fa[i]==i)sum++;
            if(in[i]>1)flag=false;
        }
        if(sum>1)
        {
            flag=false;
        }
        if(flag)
        {
            cout<<"it is a tree"<<endl;
        }
        else
        {
            cout<<"it is not a tree"<<endl;
        }
    }
    return 0;
}
