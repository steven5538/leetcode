from itertools import combinations

class Solution(object):
    def combine(self, n, k):
        return list(combinations(range(1, n + 1), k))
        