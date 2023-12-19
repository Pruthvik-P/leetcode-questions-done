class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        i=0
        j=n-1
        k=[0]*2
        while i<j:
            if numbers[i]+numbers[j]==target:
                k[0]=i+1
                k[1]=j+1
                return k
            elif numbers[i]+numbers[j]>target:
                j-=1
            else:
                i+=1

                
        
        
