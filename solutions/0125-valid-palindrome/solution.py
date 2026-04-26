class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanStr = ""
        for char in s:
            if char.isalpha():
                cleanStr += char.lower()
            elif char.isnumeric():
                cleanStr += char
        return cleanStr[::-1] == cleanStr
