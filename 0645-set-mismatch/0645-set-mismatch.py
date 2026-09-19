class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n=len(nums)
        res=[0]*(n+1)
        for i in nums:
            res[i]+=1
        rep,miss=0,0
        for i in range(1,n+1):
            if res[i]==2:
                rep=i
            elif res[i]==0:
                miss=i
        return [rep,miss]