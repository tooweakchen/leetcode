/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
        ListNode* tou=new ListNode(0);
        ListNode* wei=tou;
        int jinwei =0;
        while(l1!=NULL || l2!=NULL)
        {
            int sum1=0;
            if(l1!=NULL)
            {
                sum1=l1->val;
                l1=l1->next;
            }
            int sum2=0;
            if(l2!=NULL)
            {
                sum2=l2->val;
                l2=l2->next;
            }
            int sum3;
            sum3=sum1+sum2+jinwei;
            wei->next=new ListNode(sum3%10);
            jinwei=sum3/10;
            wei=wei->next;
        }
        if(jinwei==1)
        {
            wei->next=new ListNode(1);
        }
        return tou->next;

    }
};
