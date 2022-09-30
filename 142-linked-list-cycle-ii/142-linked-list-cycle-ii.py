# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def find_start(tortoise, head):
            curr = head
            while True:
                if curr == tortoise:
                    return curr
                curr, tortoise = curr.next, tortoise.next
            
        tortoise, hare = head, head
        while hare and hare.next:
            tortoise, hare = tortoise.next, hare.next.next
            if tortoise == hare:
                return find_start(tortoise, head)
        return None