from collections import defaultdict

class Solution(object):
    def getHint(self, secret, guess):
        A = 0
        sd = defaultdict(int)
        gd = defaultdict(int)
        
        for s, g in zip(secret, guess):
            if s == g:
                A += 1
            else:
                sd[s] += 1
                gd[g] += 1
        
        B = sum([min(sd[i], gd[i]) for i in sd])
            
        return '%dA%dB' % (A, B)
