class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        current_wealth = 0
        for i in accounts:
            current_wealth = sum(i)
            if current_wealth > max_wealth :
                max_wealth = current_wealth

        return max_wealth
        
