class Solution:
    def sortedSquares(self, s: List[int]) -> List[int]:
        res = [0]*len(s)
        i = 0
        j = len(s) - 1
        k = len(s) - 1
        while i <= j:
            if abs(s[i]) > abs(s[j]):
                res[k] = s[i]*s[i]
                i += 1
            else:
                res[k] = s[j]*s[j]
                j -= 1
            k -= 1
        return res