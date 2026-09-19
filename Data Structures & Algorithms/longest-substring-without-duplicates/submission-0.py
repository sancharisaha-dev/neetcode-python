class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        left = 0
        max_len = 0
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1
            while freq[s[i]] > 1:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
            max_len = max(max_len, i-left+1)
        return max_len
        