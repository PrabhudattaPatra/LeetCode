class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        total = 0
        for j in range(k):
            total += nums[j]
        Max = total/k
        i = 0
        j = k
        while j < n:
            total += nums[j]
            total -= nums[i]
            Max = max(Max,total/k)
            i += 1
            j += 1
        return Max



