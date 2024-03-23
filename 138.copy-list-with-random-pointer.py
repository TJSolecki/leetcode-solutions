from typing import Optional


# Definition for a Node.
class Node:
    def __init__(
        self, x: int, next: "Optional[Node]" = None, random: "Optional[Node]" = None
    ):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        # strategy is to recursivley go through and create clone nodes using
        # a closure with a mem map outside of the closure
        # base case should be if its null or already copied
        copied = {}

        def dfs(head: Optional[Node]):
            if head == None:
                return None
            if head in copied:
                return copied[head]
            new_head = Node(head.val)
            copied[head] = new_head
            new_head.next = dfs(head.next)
            new_head.random = dfs(head.random)
            return new_head

        return dfs(head)
