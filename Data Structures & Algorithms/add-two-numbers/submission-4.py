# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        ans = dummy
        carry = 0

        while (l1) or (l2) or (carry != 0):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            Sum = x+y + carry
            carry = Sum // 10
            
            ans.next = ListNode(Sum%10)
            ans = ans.next
            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next



        return dummy.next