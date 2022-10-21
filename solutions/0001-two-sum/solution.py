class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            a=0
            for j in range(1,len(nums)):
                if j!=i:
                    a=nums[i]+nums[j]
                if a==target:
                    return(([i,j]))
