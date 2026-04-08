class Solution:
    def scoreOfString(self, s: str) -> int:
        l = []
        score = 0
        for i in s:
            l.append(ord(i))
        for a, b in pairwise(l):
            score += abs(a-b)
        return score
