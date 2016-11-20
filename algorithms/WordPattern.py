class Solution(object):
    def wordPattern(self, pattern, str):
        h = {}
        s = str.split()
        
        if len(s) != len(pattern):
            return False
            
        for key, value in enumerate(pattern):
            if value not in h and s[key] not in h.values():
                h[value] = s[key]
            else:
                if value not in h or h[value] != s[key]:
                    return False
        
        return True
        