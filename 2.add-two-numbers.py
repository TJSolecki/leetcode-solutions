# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        head = curr = None
        while l1 or l2 or carry != 0:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            sum = v1 + v2 + carry
            carry = 0 if sum < 10 else sum // 10
            value = sum % 10
            if head == None or curr == None:
                head = ListNode(value)
                curr = head
            else:
                curr.next = ListNode(value)
                curr = curr.next
        return head
