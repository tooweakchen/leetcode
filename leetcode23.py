#__author__ = 'tooweakchen'
#coding:utf-8
#Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists)==0:
            return None
        if len(lists)==1:
            return lists[0]

        mid=len(lists)/2
        left=self.mergeKLists(lists[:mid])
        right=self.mergeKLists(lists[mid:])

        cur1=ListNode(0)
        cur2=cur1
        while left or right:
            if right is None or (left and left.val<=right.val):
                cur2.next=left
                left=left.next
            elif left is None or(right and right.val<=left.val):
                cur2.next=right
                right=right.next
            cur2=cur2.next
        return cur1.next

