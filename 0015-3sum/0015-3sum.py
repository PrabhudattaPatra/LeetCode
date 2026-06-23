class Solution:
    def twosum(Self,f,nums,result:list[int]):
        i = f + 1
        j = len(nums) - 1
        while i < j:
            total = nums[f]+nums[i]+nums[j]
            if total == 0:
                result.append([nums[f],nums[i],nums[j]])
                while i<j and nums[i] == nums[i+1]:
                    i += 1
                while i<j and nums[j] == nums[j-1]:
                    j -= 1
                i += 1
                j -=  1
            elif total < 0:
                i += 1
            else :
                j -= 1


    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        for f in range(len(nums)-2):
            if f > 0 and nums[f] == nums[f-1]:
                continue
            self.twosum(f,nums,result)
        return result