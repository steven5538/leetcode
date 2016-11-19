class Solution(object):
    def generate(self, numRows):
        ans = []
        for i in xrange(0, numRows):
            ans.append([])
            
        for i in xrange(0, numRows):
            for j in xrange(0, i + 1):
                if i == 0 or j == i or j == 0:
                    ans[i].append(1)
                else:
                    ans[i].append(ans[i - 1][j - 1] + ans[i - 1][j])
                    
        return ans
                
        