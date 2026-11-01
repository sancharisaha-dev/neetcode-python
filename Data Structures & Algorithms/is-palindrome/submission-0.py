class Solution:
    def isPalindrome(self, s: str) -> bool:
        high = len(s) - 1
        low = 0
        while low < high :
            if not s[low].isalnum():
                low += 1
                continue
            if not s[high].isalnum():
                high -= 1
                continue
            if s[low].lower() != s[high].lower():
                return False
            high -= 1
            low +=1
        return True
        