# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import sys
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        tor, hare = head, head
        while hare and hare.next:
            tor = tor.next
            hare = hare.next.next
            if tor == hare:
                return True
        return False
        