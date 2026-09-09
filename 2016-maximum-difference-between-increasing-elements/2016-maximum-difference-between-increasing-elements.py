class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_val=nums[0]
        max_val=-1
        for i in range(1,len(nums)):
            if nums[i]>min_val:
                max_val=max(max_val,nums[i]-min_val)
            else:
                min_val=nums[i]
        return max_val
