# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        curr = head

        while curr:
            l +=1
            curr = curr.next

        dummy = ListNode(0)
        dummy.next = head

        node = dummy

        for _ in range(l - n):
            node = node.next

        node.next = node.next.next

        return dummy.next