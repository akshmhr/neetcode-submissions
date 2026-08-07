# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        rt = root
        while rt:
            temp = rt.val

            if (temp < p.val) and (temp < q.val):
                rt = rt.right

            elif (temp > p.val) and (temp > q.val):
                rt = rt.left
            
            else:
                return rt

