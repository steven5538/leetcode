class Solution(object):
    def romanToInt(self, s):
        romans = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        ans = 0
        
        for i in range(0, len(s) - 1):
            if romans[s[i]] < romans[s[i + 1]]:
                ans -= romans[s[i]]
            else:
                ans += romans[s[i]]
                
        return ans + romans[s[-1]]
            
