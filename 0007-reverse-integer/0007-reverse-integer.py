class Solution(object):
    def reverse(self, x):

        isNegative = x < 0
        x =  abs(x)

        reverse = 0

        while x > 0:
            digit = x % 10
            reverse = (reverse  * 10) + digit
            x = x // 10

        result = -reverse if isNegative else reverse

        if result < -2**31 or result > 2**31 - 1:
            return 0
        else:
            return result