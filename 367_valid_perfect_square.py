class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if (num % 4) not in (0, 1):
            return False

        x = num
        while x*x > num:
            x = (x + num/x) / 2
        return x*x == num
