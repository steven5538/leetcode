class Solution(object):
    def convertToTitle(self, n):
        answer = ''
        while n > 0:
            answer += chr(ord('A') + ((n - 1) % 26))
            n = (n - 1) / 26
            
        return answer[::-1]
        