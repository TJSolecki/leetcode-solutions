# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return None

        fast, slow = head, head

        for _ in range(n):
            fast = fast.next

        if fast == None:
            return slow.next

        while fast != None:
            fast = fast.next
            if fast == None:
                slow.next = slow.next.next
            else:
                slow = slow.next

        return head
