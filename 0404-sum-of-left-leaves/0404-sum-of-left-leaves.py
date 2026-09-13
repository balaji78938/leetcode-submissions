# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sum=0
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def getSum(root):
            if root:
                if root.left:
                    if not root.left.left and not root.left.right:
                        self.sum+=root.left.val
                getSum(root.left)
                getSum(root.right)
        getSum(root)
        return self.sum
        