#__author__ = 'tooweakchen'
#coding:utf-8
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        cur1=ListNode(0)
        cur2=cur1
        while l1 and l2:
            if l1.val<=l2.val:
                cur2.next=l1
                l1=l1.next
            elif l1.val>l2.val:
                cur2.next=l2
                l2=l2.next
            cur2=cur2.next
        cur2.next=l1 or l2
        return cur1.next