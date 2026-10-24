class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        res =  nums[0]

        for i in range(1, len(nums)):
            curr_val = nums[i]

            curr_max, curr_min = max(curr_val, curr_max * curr_val, curr_min * curr_val), min(curr_val, curr_max * curr_val, curr_min * curr_val)
            res = max(res, curr_max)
        return res