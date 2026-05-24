# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = node = ListNode()
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        i = 0
        j = len(nodes) - 1
        while i <= j:
            node.next = nodes[i]
            i += 1
            node = node.next
            node.next = nodes[j]
            j -= 1
            node = node.next

        node.next = None
        