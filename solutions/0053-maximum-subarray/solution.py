class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        Max = -99999
        Sum = 0
        for i in range(len(nums)):
            Sum += nums[i]
            if Sum > Max:
                Max = Sum
            if Sum < 0:
                Sum = 0
        return Max  
        
        
