class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq ={}
        max_freq = 0
        max_len = 0
        for i in range(len(s)) :
            freq[s[i]] = freq.get(s[i], 0) + 1
            max_freq = max(max_freq, freq[s[i]])
            #window_size = i-left+1
            while (i-left+1) - max_freq > k :
                freq[s[left]] -= 1
                left += 1
            max_len = max(max_len, i-left+1)
        return max_len

        