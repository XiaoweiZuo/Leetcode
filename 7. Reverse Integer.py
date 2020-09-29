class Solution:
    def reverse(self, x: int) -> int:
        # # method 1: math approach
        # a = abs(x)
        # rev = 0
        # while a != 0:
        #     rev = rev * 10 + a % 10
        #     a = a // 10
        
        # if ( (-2**31) <= rev <= (2**31 -1) ) :
        #     return -rev if x < 0 else rev
        # else:
        #     return 0




        # method 2: string approach
        if x >= 0:
            a = x
        else:
            a = -x

        rev = int(str(a)[::-1])

        # the rest is the same as in math approach
        if ( (-2**31) <= rev <= (2**31 -1) ) :
            return -rev if x < 0 else rev
        else:
            return 0