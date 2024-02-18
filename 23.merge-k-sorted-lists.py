class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None

        while len(lists) > 1:
            temp_lists = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if (i + 1) < len(lists) else None
                temp_lists.append(self.merge_lists(list1, list2))

            lists = temp_lists

        return lists[0]

    def merge_lists(self, list1, list2):
        dummy = new_list = ListNode(0, None)
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                new_list.next = list1
                list1 = list1.next
            else:
                new_list.next = list2
                list2 = list2.next
            new_list = new_list.next

        if list1 == None and list2 != None:
            new_list.next = list2
        elif list2 == None and list1 != None:
            new_list.next = list1

        return dummy.next
