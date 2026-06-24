# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return
        length = len(preorder)
        i = 0
        while i < length and inorder[i] != preorder[0]:
            i += 1
        root = TreeNode()
        root.val = inorder[i]
        left = inorder[:i]
        right = inorder[i+1:]
        left_preorder = preorder[1:i+1]
        right_preorder = preorder[i+1:]
        root.left = self.buildTree(left_preorder, left)
        root.right = self.buildTree(right_preorder, right)
        return root

