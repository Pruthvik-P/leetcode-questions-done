class Solution:
    def reverse(self, x: int) -> int:
        revNum=0
        n=abs(x)
        while n>0:
            s=n%10
            revNum=(revNum*10)+s
            n//=10
        if revNum in range(-2**31,2**31-1):
            if (x<0):
                revNum=(revNum - revNum * 2)
                return revNum
            return revNum
        return 0

       

        
        
