class Solution(object):
    def isUgly(self, num):
        if num <= 0:
            return False
        elif num == 1 or num == 2 or num == 3 or num == 5:
            return True
        elif num % 2 == 0:
            return self.isUgly(num / 2)
        elif num % 3 == 0:
            return self.isUgly(num / 3)
        elif num % 5 == 0:
            return self.isUgly(num / 5)
        else:
            return False
        
        