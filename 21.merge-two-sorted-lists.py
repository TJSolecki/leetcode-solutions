# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        new_list = None
        new_list_head = None
        while list1 != None and list2 != None:
            if list2.val < list1.val:
                if new_list == None:
                    new_list_head = list2
                    new_list = list2
                else:
                    new_list.next = list2
                    new_list = list2
                list2 = list2.next
            else:
                if new_list == None:
                    new_list_head = list1
                    new_list = list1
                else:
                    new_list.next = list1
                    new_list = list1
                list1 = list1.next

        if new_list != None and list2 != None and list1 == None:
            new_list.next = list2

        if new_list != None and list1 != None and list2 == None:
            new_list.next = list1

        return new_list_head
