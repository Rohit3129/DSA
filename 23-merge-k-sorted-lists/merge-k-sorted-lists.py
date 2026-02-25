# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i,  node))
        d = ListNode()
        curr = d
        while heap:
            val, i ,node = heapq.heappop(heap)
            curr.next = node
            curr = node
            node =  node.next
            if node:
                heapq.heappush(heap, (node.val, i,  node))
        return d.next
