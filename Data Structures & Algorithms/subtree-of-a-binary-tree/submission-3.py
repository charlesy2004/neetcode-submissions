# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        def sameTree(root, subRoot):
            if (root is None and subRoot is not None) or (root is not None and subRoot is None):
                return False
            if root is None and subRoot is None:
                return True
            if root.val == subRoot.val:
                Left = sameTree(root.left, subRoot.left)
                Right = sameTree(root.right, subRoot.right)
                return Left and Right
            return False
       
        if sameTree(root, subRoot):
            return True
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
        