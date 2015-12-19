class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        pre_length = 0
        length = 0

        for c in s:
            if c == ' ':
                if length != 0:
                    pre_length = length
                    length = 0
            else:
                length += 1

        if not length:
            return pre_length
        else:
            return length
