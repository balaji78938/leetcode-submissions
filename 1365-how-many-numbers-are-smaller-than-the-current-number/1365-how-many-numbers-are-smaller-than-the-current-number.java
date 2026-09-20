class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int n=nums.length;
        int res[]=new int[n];
        int sort[]=new int[n];
        System.arraycopy(nums,0,sort,0,n);
        Arrays.sort(sort);
        for(int i=0;i<n;i++){
            int num=nums[i],count=0;
            for(int j=0;j<n;j++){
                if(num==sort[j]){
                    res[i]=j;
                    break;
                }
            }
        }
        return res;
    }
}