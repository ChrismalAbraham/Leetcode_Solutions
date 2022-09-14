# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list_length = 0
        node = head
        while node is not None:
            list_length += 1
            node = node.next
        node = head
        for i in range((list_length // 2)):
            node = node.next
        return node