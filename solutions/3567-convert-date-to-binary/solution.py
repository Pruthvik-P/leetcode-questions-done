class Solution:
    def convertDateToBinary(self, date: str) -> str:
        dec = [int(x) for x in date.split("-")]
        bi = []
        for i in dec:
            temp = ""
            while i > 0:
                temp += str(i % 2)
                i //= 2
            bi.append(temp[::-1])
        return "-".join(bi)
