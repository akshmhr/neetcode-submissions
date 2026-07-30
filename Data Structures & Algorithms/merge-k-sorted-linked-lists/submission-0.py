# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for ls in lists:
            while ls:
                heapq.heappush(heap, ls.val)
                ls = ls.next

        
        dummy = ListNode()
        merge = dummy
        for i in range(len(heap)):
            node = ListNode(heapq.heappop(heap))
            merge.next = node
            merge = merge.next


        return dummy.next


            




