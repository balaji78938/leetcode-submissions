class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        if n <= 2:
            return nums
        suffix_max = [0] * n
        suffix_max[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(nums[i], suffix_max[i + 1])
        res = [nums[0]] 
        prefix_max = nums[0]
        for i in range(1, n - 1):
            if nums[i] > prefix_max or nums[i] > suffix_max[i + 1]:
                res.append(nums[i])
            prefix_max = max(prefix_max, nums[i])
        res.append(nums[-1])
        return res