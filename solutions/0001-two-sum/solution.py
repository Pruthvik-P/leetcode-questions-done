class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num=sorted(nums)
        i=0
        j=len(nums)-1
        while i<j:
            if num[i]+num[j]==target:


                k=[k for k in range(len(nums)) if nums[k]==num[i] or nums[k]==num[j]]
                
                return k
            
            elif num[i]+num[j]<target:
                i+=1
            else:
                j-=1
