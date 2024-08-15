class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, count = 0, 0
        for i in nums:
            count = (count + 1) if i == 1 else 0
            res = max(res, count)
        return res
