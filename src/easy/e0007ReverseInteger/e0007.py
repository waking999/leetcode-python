import sys


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max = 2 ** 31 - 1

        min = -2 ** 31

        y = 0
        isNeg = False
        if x < 0:
            isNeg = True
            x = -x

        while x != 0:
            y = y * 10 + x % 10
            x //= 10
            if y > max or y < min:
                return 0

        return y if not isNeg else -y
