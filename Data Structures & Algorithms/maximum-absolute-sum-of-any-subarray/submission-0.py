class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        res = abs(nums[0])

        for i in range(1, len(nums)):
            x = nums[i]
            curr_max = max(x, curr_max + x)
            curr_min = min(x, curr_min + x)
            res = max(res, abs(curr_max), abs(curr_min))
        return res
