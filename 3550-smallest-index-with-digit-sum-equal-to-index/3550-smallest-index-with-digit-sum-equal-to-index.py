class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def dig_sum(n):
            sum=0
            while n>0:
                sum+=n%10
                n//=10
            return sum
        for i,val in enumerate(nums):
            if i== dig_sum(val):
                return i
        return -1