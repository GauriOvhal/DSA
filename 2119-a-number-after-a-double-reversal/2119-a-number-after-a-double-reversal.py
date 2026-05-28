class Solution(object):
    def isSameAfterReversals(self, num):

        reverse_num1 = self.reverse(num)
        reverse_num2 =  self.reverse(reverse_num1)
        if reverse_num2 == num:
            return True
        else:
            return False

    def reverse(self ,x):
        isNegative = x < 0
        x =  abs(x)

        reverse = 0

        while x > 0:
            digit = x % 10
            reverse = (reverse  * 10) + digit
            x = x // 10

        return -reverse if isNegative else reverse
        