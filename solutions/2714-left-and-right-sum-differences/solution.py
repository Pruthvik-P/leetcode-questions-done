class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        difference = [0] * n
        right = [0] * n
        left = [0] * n

        left[0] = nums[0]
        for i in range(1,n):
            left[i] = left[i-1] + nums[i]
        
        right[n-1] = nums[n-1]
        for i in range(n-2,-1,-1):
            right[i] = right[i+1] + nums[i]
        
        for i in range(n):
            difference[i] = abs(left[i] - right[i])

        return difference

        
