/*
    �����Ŀ��˼�Ƚϼ򵥣�������Ҫ��������û�����������Ĵ�С��
    ����һ��ʼ����O(n2)�ķ������ģ����潻��ȥ��ʱ��Ȼ���뵽����������
    ��Ϊ�����ʱ�临�Ӷ���nlgn��Ȼ����ͷ��ʼ�ң�����o(n),���Եڶ��ַ�����
    ʱ�临�ӶȻ���nlgn��
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
