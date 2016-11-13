class Solution(object):
    def firstUniqChar(self, s):
        characters = 'abcdefghijklmnopqrstuvwxyz'
        unique = [s.index(i) for i in characters if s.count(i) == 1]
        return min(unique) if len(unique) > 0 else -1