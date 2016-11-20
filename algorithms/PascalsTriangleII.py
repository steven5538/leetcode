import math

class Solution(object):
    def getRow(self, rowIndex):
        answer = []
        
        if rowIndex == 0:
            return [1]
            
        top = math.factorial(rowIndex)
        for i in xrange(0, rowIndex + 1):
            down = math.factorial(i) * math.factorial(rowIndex - i)
            answer.append(int(top / down))
            
        return answer
            