class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max1=0
        cur=0
        for i in nums:
            if i==1:
                cur+=1
            else:
                max1=max(max1,cur)
                cur=0
        return max(max1,cur)
