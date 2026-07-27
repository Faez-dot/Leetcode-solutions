class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x<0 else 1
        x=abs(x)

        reversed_num=0
        while x!=0:
            #Extract last digit
            digit = x%10
            #Append
            reversed_num = reversed_num*10 + digit
            #truncate last digit out of x
            x//=10
        reversed_num*=sign
        if reversed_num < -2147483649 or reversed_num > 2147483647:
            return 0
        return reversed_num