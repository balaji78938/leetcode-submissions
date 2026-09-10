# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count=0
        self.postOrder(root)
        return self.count
    
    def postOrder(self,root):
        if not root:
            return 0,0
        left_sum,left_count=self.postOrder(root.left)
        right_sum,right_count=self.postOrder(root.right)
        cur_sum=left_sum+right_sum+root.val
        cur_count=left_count+right_count+1
        if cur_sum // cur_count==root.val:
            self.count+=1
        return cur_sum,cur_count