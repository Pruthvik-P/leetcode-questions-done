from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mpp = defaultdict(int)
        preSum = 0
        count = 0

        mpp[0] = 1
        for i in range(n):
            preSum += nums[i]
            remove = preSum - k
            count += mpp[remove]
            mpp[preSum] += 1
        return count
        
