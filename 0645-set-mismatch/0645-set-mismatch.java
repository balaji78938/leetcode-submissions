class Solution {
    public int[] findErrorNums(int[] nums) {
        int n=nums.length;
        int freq[]=new int[n+1];
        for(int i:nums)
            freq[i]++;
            int rep=0,mis=0;
        for(int i=1;i<n+1;i++){
            if(freq[i]==2)
                rep=i;
            else if(freq[i]==0)
                mis=i;
        }
        return new int[]{rep,mis};
    }
}