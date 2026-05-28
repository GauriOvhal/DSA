class Solution(object):
    def reverseBits(self, n):

        binary_n =  self.decToBinary(n)

        binary_n = binary_n.zfill(32)

        reversed_binary = binary_n[::-1]

        return int(reversed_binary, 2)

    def decToBinary(self , n):
        if n == "0":
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