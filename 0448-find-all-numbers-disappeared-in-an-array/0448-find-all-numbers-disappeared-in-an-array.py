class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        res=[]
        n=len(nums)
        s=set(nums)
        for i in range(1,n+1):
            if i not in s:
                res.append(i)
        return res