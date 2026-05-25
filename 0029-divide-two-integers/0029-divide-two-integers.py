class Solution(object):
    def divide(self, dividend, divisor):

        # Handle overflow case
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        # Determine sign
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        # Convert to positive
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:

            temp = divisor
            multiple = 1

            # Keep doubling
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            quotient += multiple

        return sign * quotient