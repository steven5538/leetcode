class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        left = max(A, E)
        bottom = max(B, F)
        right = max(min(C, G), left)
        top = max(min(D, H), bottom)
        return abs(C - A) * abs(D - B) + abs(G - E) * abs(H - F) - abs(right - left) * abs(top - bottom)
        
        