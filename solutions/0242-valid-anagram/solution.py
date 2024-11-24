class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = [i for i in s]
        t1 = [i for i in t]
        s1.sort()
        t1.sort()
        return s1 == t1
        
