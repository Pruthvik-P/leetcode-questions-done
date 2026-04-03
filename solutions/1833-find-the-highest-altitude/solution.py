class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxHeight = 0
        currentHeight = 0
        for i in gain:
            currentHeight += i
            if currentHeight > maxHeight:
                maxHeight = currentHeight
        return maxHeight

