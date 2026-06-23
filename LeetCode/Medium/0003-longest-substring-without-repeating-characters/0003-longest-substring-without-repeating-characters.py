class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Max = 0
        i = 0  # Left pointer of the window
        n = len(s)
        seen = set()
        
        for j in range(n):  # j acts as the right pointer
            # 1. Shrink the window from the left until the duplicate character is gone
            while s[j] in seen:
                seen.remove(s[i])
                i += 1  # Crucial: move the left boundary forward
            
            # 2. Add the current character to the valid window
            seen.add(s[j])
            
            # 3. Calculate the length of the current valid window (j - i + 1)
            Max = max(Max, j - i + 1)
            
        return Max