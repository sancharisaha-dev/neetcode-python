class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        pass
        freq = {0:-1}
        max_len = 0
        prefix = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                prefix -= 1
            else:
                prefix += 1
            if prefix in freq:
                max_len = max(max_len, i-freq[prefix])
            else:
                freq[prefix] = i
        return max_len
