class Solution(object):
    def hammingWeight(self, n):

        binary_n = self.decToBinary(n)

        count = 0
        for ch in str(binary_n):
            digit = int(ch)
            if digit == 1:
                count += 1

        return count

    def decToBinary(self , n):
        if n == 0:
            return 0

        isNegative = n < 0
        n = abs(n)

        remainders_list = []

        while n > 0:
            remainder = n % 2
            remainders_list.append(str(remainder))
            n =  n // 2

        remainders_list.reverse()
        binary_string = "".join(remainders_list)

        return "-"+binary_string if isNegative else binary_string
        