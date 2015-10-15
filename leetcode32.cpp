class Solution {
public:
    int longestValidParentheses(string s) {
        stack<int>s1;
        bool *a = new bool[s.length()];
        memset(a,false,s.length());
        for(int i=0; i<s.length(); i++){
            if(s[i]=='('){
                s1.push(i);
            }
            else if(s[i]==')'&&!s1.empty()){
                a[i]=true;
                a[s1.top()]=true;
                s1.pop();
            }
        }
        int max1=0,sum=0;
        for(int i=0; i<s.length(); i++){
            if(a[i])sum++;
            else sum=0;
            max1=max(max1,sum);
        }
        return max1;
    }
};
