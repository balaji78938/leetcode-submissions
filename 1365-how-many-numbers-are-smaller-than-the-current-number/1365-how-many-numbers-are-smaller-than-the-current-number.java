class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int n=nums.length;
        int res[]=new int[n];
        for(int i=0;i<n;i++){
            int num=nums[i],count=0;
            for(int n1:nums){
                if(num>n1)
                    count++;
            }
            res[i]=count;
        }
        return res;
    }
}