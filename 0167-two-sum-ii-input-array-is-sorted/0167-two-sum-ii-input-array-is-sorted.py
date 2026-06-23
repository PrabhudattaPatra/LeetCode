class Solution:
    def twoSum(self, s: List[int], target: int) -> List[int]:
        i = 0
        j = len(s) -1 
        while i < j:
            total = s[i]+s[j]
            if total == target:
                return [i+1,j+1]
            elif total > target:
                j -= 1
            else:
                i += 1
        return [0,0]

