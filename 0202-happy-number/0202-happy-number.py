class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        visited = set()

        while n not in visited:
            if n == 1:
                return True

            visited.add(n)

            total = 0

            while n > 0:
                digit = n % 10
                total += digit * digit
                n =  n // 10

            n = total

        return False