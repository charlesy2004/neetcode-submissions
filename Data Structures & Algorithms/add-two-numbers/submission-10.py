# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur_l1 = l1
        cur_l2 = l2
        addover = 0
        dummy = ListNode(0)
        curr = dummy
        while cur_l1 and cur_l2:
            sums = cur_l1.val + cur_l2.val + addover
            
            
            addover = sums // 10
            cur_l1 = cur_l1.next
            cur_l2 = cur_l2.next
                

            curr.next = ListNode(sums % 10)

            curr = curr.next
        while cur_l1:
            sums = cur_l1.val + addover
            addover = sums // 10
            curr.next = ListNode(sums % 10)
            curr = curr.next
            cur_l1 = cur_l1.next
        while cur_l2:
            sums = cur_l2.val + addover
            addover = sums // 10
            curr.next = ListNode(sums % 10)
            curr = curr.next
            cur_l2 = cur_l2.next
        if addover:
            curr.next = ListNode(addover)
            curr = curr.next
        return dummy.next



        


