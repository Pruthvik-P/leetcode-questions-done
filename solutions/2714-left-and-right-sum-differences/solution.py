class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        diffSum = [0] * len(nums)
        leftSum = 0
        rightSum = sum(nums)

        for i in range(len(nums)):
            rightSum -= nums[i]
            diffSum[i] = abs(leftSum - rightSum)
            leftSum += nums[i] 

        return diffSum
