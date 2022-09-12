# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def find_cycle_start(head, tor):
            tracker = head
            while tracker:
                if tracker == tor: return tracker
                tracker = tracker.next
                tor = tor.next
        tor, hare = head, head
        while hare and hare.next:
            tor = tor.next
            hare = hare.next.next
            if tor == hare:
                return find_cycle_start(head, tor)
        return None