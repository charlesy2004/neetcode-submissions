# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        count = 0
        q = deque([(root, root.val)])
        while q:
            curr_node, path_max = q.popleft()
            if curr_node and curr_node.val >= path_max:
                
                count += 1
            pathmax = max(curr_node.val, path_max)
            if curr_node.right:
                q.append((curr_node.right, pathmax))
            if curr_node.left:
                q.append((curr_node.left, pathmax))
            
            
        return count