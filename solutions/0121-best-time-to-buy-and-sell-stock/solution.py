class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = 0
        minPro = 99999
        for i in range(len(prices)):
            minPro = min(minPro, prices[i])
            maxPro = max(maxPro, prices[i] - minPro)
        return maxPro
        
