# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], p: int, q: int) -> Optional[ListNode]:
        if p == q:
            return head

        prev, curr = None, head
        i = 0
        while curr != None and i < p - 1:
            prev = curr
            curr = curr.next
            i += 1
        end_of_first_list = prev
        end_of_sub_list = curr

        i = 0
        while curr != None and i < q - p + 1:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            i += 1

        if end_of_first_list != None:
            end_of_first_list.next = prev
        else:
            head = prev
        end_of_sub_list.next = curr
        return head
        