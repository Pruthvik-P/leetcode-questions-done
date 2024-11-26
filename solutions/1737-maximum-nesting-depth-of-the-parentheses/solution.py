class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        opened = 0

        for i in s:
            if i == "(":
                opened += 1
                ans = max(ans, opened)
            elif i ==")":
                opened -= 1
        return ans
        
