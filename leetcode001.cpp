/*
    这个题目意思比较简单，但是主要的问题是没告诉这个数组的大小；
    所以一开始我用O(n2)的方法做的，后面交上去超时，然后想到可以先排序；
    因为排序的时间复杂度是nlgn，然后两头开始找，这样o(n),所以第二种方法的
    时间复杂度还是nlgn。
*/

struct node
{
    int zhi;
    int pos;
};

bool cmp(node a,node b)
{
    return a.zhi<b.zhi;
}

class Solution
{
public:
    vector<int> twoSum(vector<int> &numbers, int target)
    {
        vector<int>v;
        vector<node>arr;
        for(int i=0; i<numbers.size(); i++)
        {
            node num;
            num.zhi=numbers[i];
            num.pos=i;
            arr.push_back(num);
        }
        sort(arr.begin(),arr.end(),cmp);
        for(int i=0,j=arr.size()-1; i!=j;)
        {
            int sum=arr[i].zhi+arr[j].zhi;
            if(sum==target)
            {
                if(arr[i].pos>arr[j].pos)
                {
                    v.push_back(arr[j].pos+1);
                    v.push_back(arr[i].pos+1);
                }
                else
                {
                    v.push_back(arr[i].pos+1);
                    v.push_back(arr[j].pos+1);
                }
                break;
            }
            else
            {
                if(sum<target)
                {
                    i++;
                }
                else if(sum>target)
                {
                    j--;
                }
            }
        }
        return v;
    }
};
