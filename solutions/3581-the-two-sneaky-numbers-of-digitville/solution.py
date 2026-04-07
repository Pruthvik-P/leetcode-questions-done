class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        mis = []
        res = []
        for i in nums:
            if i not in mis :
                mis.append(i)
            elif i in mis:
                res.append(i)

        return res
