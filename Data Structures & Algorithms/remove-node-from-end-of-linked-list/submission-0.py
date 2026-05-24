# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, curr = None, head

        # reverse the list
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        curr1 = prev
        pre = curr1
        if n == 1:
            curr1 = curr1.next
        else:
            for i in range(n - 2):
                pre = pre.next
            pre.next = pre.next.next
        prev1, curr2 = None, curr1
        # del from list
        # reverse list again
        while curr2:
            temp = curr2.next
            curr2.next = prev1
            prev1 = curr2
            curr2 = temp
        return prev1

