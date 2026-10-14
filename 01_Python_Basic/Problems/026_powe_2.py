
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        Check whether n is a power of two.

        A power of two is a number like:
        1, 2, 4, 8, 16, 32, 64, ...

        Rule:
        A positive number n is a power of two if:
        (n & (n - 1)) == 0
        """

        # Step 1: A power of two must be positive.
        # This rejects 0 and all negative numbers.
        if n <= 0:
            return False

        # Step 2: Check whether n has exactly one set bit (1)
        # in its binary representation.
        #
        # n & (n - 1) removes the rightmost set bit.
        # If the result is 0, n had only one set bit.
        if (n & (n - 1)) == 0:
            return True

        # Step 3: If more than one set bit exists,
        # n is not a power of two.
        return False
