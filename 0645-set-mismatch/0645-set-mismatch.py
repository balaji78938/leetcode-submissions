class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        mini=min(nums)
        maxi=max(nums)
        if mini==maxi==1:
            return[1,2]
        if mini==maxi:
            return[mini,maxi-1]
        res=[0 for i in range(0,maxi+2)]
        for i in nums:
            res[i]+=1
            rep,miss=0,0
        for i in range(1,maxi+2):
            if res[i]==2:
                rep=i
            if miss==0 and res[i]==0:
                miss=i
        return [rep,miss]