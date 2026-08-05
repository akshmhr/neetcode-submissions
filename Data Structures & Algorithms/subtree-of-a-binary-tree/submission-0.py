# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSame(self, s, q):
        if (not s) and (not q):
            return True
        if (not s) or (not q):
            return False

        if s.val != q.val:
            return False
        
        return self.isSame(s.left, q.left) and self.isSame(s.right, q.right)



    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if self.isSame(root, subRoot):
            return True


        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)