# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev , curr = None , head
        # None 1 2 3 4
        while curr: 
            temp = curr.next #2 #3
            curr.next = prev #None #1
            prev = curr #1 #2
            curr = temp #2 #3
        return prev
        