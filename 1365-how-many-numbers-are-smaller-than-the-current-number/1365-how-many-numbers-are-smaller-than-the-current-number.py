class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        n=sorted(nums)
        res=[]
        for i in nums:
            res.append(n.index(i))
        return res