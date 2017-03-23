class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.upper() == word:
            return True
        elif word[1:].lower() == word[1:]:
            return True
        else:
            return False
