class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # subtract (keeping only positive counts)
        return not collections.Counter(ransomNote) - collections.Counter(magazine)
