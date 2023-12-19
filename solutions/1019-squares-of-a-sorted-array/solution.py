class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i=0
        j=len(nums)-1
        k=[0]*len(nums)
        m=len(nums)-1
        while i<=j:
            if abs(nums[i])>abs(nums[j]):
                k[m]=nums[i]**2
                i+=1
            else:
                k[m]=nums[j]**2
                j-=1
            m-=1
        print(k)
        return k
                
        
