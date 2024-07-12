class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:

        maxOnesCount,maxOnesIdx = 0, 0

        for i, row in enumerate(mat):
            onesCount = sum(row)
            
            if onesCount > maxOnesCount :
                maxOnesCount, maxOnesIdx = onesCount, i
        
        return [maxOnesIdx, maxOnesCount]
        
