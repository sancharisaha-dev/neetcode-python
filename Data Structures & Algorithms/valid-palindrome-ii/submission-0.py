class Solution:
    def validPalindrome(self, s: str) -> bool:
        high = len(s)-1
        low = 0
        while low < high :
            if s[low] != s[high] :
                i = low + 1
                j = high
                
                while i<j and s[i]==s[j]:
                    i+=1
                    j-=1
                if i>=j:
                    return True
                
                i = low
                j = high - 1
                
                while i<j and s[i] == s[j]:
                    i +=1
                    j -=1
                return i>=j
            low +=1
            high -= 1
        return True
        