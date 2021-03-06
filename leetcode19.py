#__author__ = 'tooweakchen'
#coding:utf-8
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        dummy=ListNode(0)
        dummy.next=head
        fast=dummy
        slow=dummy
        while n>0:
            fast=fast.next
            n-=1
        while fast.next:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return dummy.next
