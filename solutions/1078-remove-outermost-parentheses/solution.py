class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        opened = 0
        for i in s:
            if i == "(":
                opened += 1
                if opened > 1:
                    res.append(i)
            else: 
                opened -= 1
                if opened > 0:
                    res.append(i)

        return "".join(res)

        
