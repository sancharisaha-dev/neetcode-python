class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        tf = {}
        sf = {}
        min_len = float("inf")
        have = 0
        res = ""

        for ch in t:
            tf[ch] = tf.get(ch, 0) + 1
        need = len(tf)

        for i in range(len(s)):
            sf[s[i]] = sf.get(s[i], 0) + 1

            if s[i] in t and sf[s[i]] == tf[s[i]]:
                have += 1
            
            while have == need :
                if i-left+1 < min_len :
                    min_len = i - left + 1
                    res = s[left:i + 1]
                sf[s[left]] -= 1
                
                if s[left] in t and sf[s[left]] < tf[s[left]]:
                    have -= 1
                left += 1
        return res



        
        