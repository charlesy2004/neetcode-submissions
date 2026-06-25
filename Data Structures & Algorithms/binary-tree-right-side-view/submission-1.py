# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        # look at q
        # pop first element
        # if it has right element
        # pop all current elements and add all their children to queue
        #
        q = deque([root])
        res = []
        while q:
            length = len(q)
            for i in range(length):
                curr_node = q.popleft()
                if i == 0:
                    res.append(curr_node.val)
                if curr_node.right:
                    q.append(curr_node.right)
                if curr_node.left:

                    q.append(curr_node.left)
            
        
        return res


            




        