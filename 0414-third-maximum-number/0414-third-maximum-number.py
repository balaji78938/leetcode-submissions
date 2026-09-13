class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique = set(nums)
        if len(unique) < 3:
            return max(unique)
        return heapq.nlargest(3, unique)[-1]
