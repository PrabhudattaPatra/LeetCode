class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i , k , j = 0,0,len(nums)-1
        while k <= j:
            if nums[k] == 0:
                nums[i],nums[k] = nums[k],nums[i]
                i += 1
                k += 1
            elif nums[k] == 1:
                k += 1
            else:
                nums[j],nums[k] = nums[k],nums[j]
                j -= 1
        return nums
