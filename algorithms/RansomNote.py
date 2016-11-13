class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        magazine = list(magazine)
        for s in ransomNote:
            if s in magazine:
                magazine.pop(magazine.index(s))
            else:
                return False
        return True
        