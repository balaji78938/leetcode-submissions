class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n=len(nums)
        count=[0]*(n+1)
        for i in nums:
            count[i]=1
        return [i for i in range(1,n+1) if count[i]<1]