class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        ele = None

        for i in range(n):
            if count == 0:
                count += 1
                ele = nums[i]
            elif ele == nums[i]:
                count += 1
            else:
                count -=1
        
        count_1 = 0
        for i in range(n):
            if nums[i] == ele:
                count_1 += 1
        
        if count_1 >(n/2):
            return ele
        
