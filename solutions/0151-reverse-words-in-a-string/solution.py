class Solution:
    def reverseWords(self, s: str) -> str:
        k = s.split()
        reversed_string = ""
        for i in k[::-1]:
            reversed_string += i 
            reversed_string += " "
        return reversed_string.strip()
        
