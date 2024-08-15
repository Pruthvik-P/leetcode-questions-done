class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        k = len(nums)
        summ = (k*(k+1)) // 2
        return summ - sum(nums)
        
