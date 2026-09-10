/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int total_count=0;
    public int averageOfSubtree(TreeNode root) {
        dfs(root);
        return total_count;
    }
    public int[] dfs(TreeNode root){
        if(root==null)
            return new int[]{0,0};
        int left[]=dfs(root.left);
        int right[]=dfs(root.right);
        int total=left[0]+right[0]+root.val;
        int count=left[1]+right[1]+1;
        if(total/count == root.val)
            total_count++;
        return new int[]{total,count};
    }
}