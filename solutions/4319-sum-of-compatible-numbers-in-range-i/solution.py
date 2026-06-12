class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        nums = []
        start = max(1, n-k)
        end = (n+k)+1
        for x in range(start, end):
            if abs(n - x) <= k and (n & x) == 0:
                nums.append(x)

        return sum(nums)
