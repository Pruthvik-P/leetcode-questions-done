class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        negNum = x < 0 
        x = abs(x)
        while x:
            lastDigit = x % 10
            result = result * 10 + lastDigit
            x = x // 10
        if result not in range(-2**31, 2**31 - 1):
            return 0
        if negNum:
            return (0 - result)
        return result

