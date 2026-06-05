# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a_length = 0
        currA = headA
        while currA:
            currA = currA.next
            a_length += 1
        b_length = 0
        currB = headB
        while currB:
            currB = currB.next
            b_length += 1
        diff = abs(a_length - b_length)
        a_Curr = headA
        b_Curr = headB
        for i in range(diff):
            if a_length > b_length:
                a_Curr = a_Curr.next
            else:
                b_Curr = b_Curr.next
        while a_Curr:
            if a_Curr == b_Curr:
                return a_Curr
            a_Curr = a_Curr.next
            b_Curr = b_Curr.next
        return None
        
        