class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digits = []
        sqrtSum = 0
        for i in str(n):
            d = int(i)
            digits.append(d)
            sqrtSum += d**2
        digitSum = sum(digits)

        return (sqrtSum - digitSum) >= 50
