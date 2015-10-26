#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;

class Solution {
public:
    void dfs(int pos,int sum,vector<int> &can,vector<int> &v,vector< vector<int> > &v1){
        int len=can.size();
        if(sum==0){
            v1.push_back(v);
            return;
        }
        if(pos>=len || sum<0){
            return;
        }
        for(int i=pos; i<can.size(); ++i){
            if(i!=pos&&can[i]==can[i-1]){
                continue;
            }
            if(sum>=can[i]){
                v.push_back(can[i]);
                dfs(i+1,sum-can[i],can,v,v1);
                v.pop_back();
            }
        }
    }
    vector<vector<int>> combinationSum2(vector<int> &candidates, int target) {
        vector<int>v;
        vector<vector<int> >v1;
        sort(candidates.begin(),candidates.end());
        dfs(0,target,candidates,v,v1);
        return v1;
    }
};
