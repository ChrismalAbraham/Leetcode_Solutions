# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def detectCycleStart(head, tor):
            hare2 = head
            while hare2:
                if hare2 == tor: return tor
                hare2 = hare2.next
                tor = tor.next
        if not head: return
        tor, hare = head, head
        while hare and hare.next:
            tor = tor.next
            hare = hare.next.next
            if tor == hare:
                return detectCycleStart(head, tor)
        return