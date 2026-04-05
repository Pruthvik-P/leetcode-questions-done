class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in s:
            if stack and stack[-1].swapcase() == i:
                stack.pop()
            else:
                stack.append(i)

        return "".join(stack)
