class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map={}
        for i,val in enumerate(nums):
            if val in map:
                return [map[val],i]
            diff=target-val
            map[diff]=i
        