class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        last_num = None
        for c in s:
            current_num = roman_map[c]
            if last_num and last_num < current_num:
                total -= 2*last_num
            last_num = current_num
            total += current_num
        return total
