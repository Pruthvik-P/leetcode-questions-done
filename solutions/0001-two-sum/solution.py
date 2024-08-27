class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = sorted(nums)
        left = 0
        right = len(nums) - 1 
        while left < right:
            if num[left] + num[right] == target:
                k=[k for k in range(len(nums)) if nums[k] == num[left] or nums[k] == num[right]]
                return k
            elif num[left] + num[right] < target:
                left += 1
            else:
                right -= 1        
