#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;

class Solution {
public:
    void dfs(int pos,int sum,vector<int> &can,vector<int> &v,vector< vector<int> > &v1){

        int len=can.size();
        if(pos>=len||sum<0){
            return;
        }
        if(sum==0){
            v1.push_back(v);
            return;
        }
        //选择这个
        v.push_back(can[pos]);
        dfs(pos,sum-can[pos],can,v,v1);
        //不选择这个
        v.pop_back();
        dfs(pos+1,sum,can,v,v1);
    }
    vector<vector<int>> combinationSum(vector<int> &candidates, int target) {
        vector<int>v;
        vector<vector<int> >v1;
        sort(candidates.begin(),candidates.end());
        dfs(0,target,candidates,v,v1);
        return v1;
    }
};
