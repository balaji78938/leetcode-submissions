class Solution {
    public int[] getConcatenation(int[] nums) {
        int n=nums.length;
        int num[]=new int[n*2];
        System.arraycopy(nums,0,num,0,n);
        System.arraycopy(nums,0,num,n,n);
        return num;
    }
}