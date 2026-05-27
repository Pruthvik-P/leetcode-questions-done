class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        senList = s.split()[:k]
        return " ".join(senList)
