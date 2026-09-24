class Solution:
    def findMin(self, nums: list[int]) -> int:
        left=0
        right=len(nums)-1
        last=nums[right]
        while left<right:
            mid = (left + right) >> 1;
            if (nums[mid] > last):
                left = mid + 1
            else:
                 right = mid
        return nums[left]