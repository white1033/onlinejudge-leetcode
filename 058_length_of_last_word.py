class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        len_str = len(s)
        # slow and fast pointers
        slow = -1
        # iterate over trailing spaces
        while slow >= -len_str and s[slow] == ' ':
            slow -= 1
        fast = slow
        # iterate over last word
        while fast >= -len_str and s[fast] != ' ':
            fast -= 1
        return slow - fast
