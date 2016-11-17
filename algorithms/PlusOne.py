class Solution(object):
    def plusOne(self, digits):
        digits[-1] += 1
        
        for i in xrange(len(digits) - 1, 0, -1):
            if digits[i] >= 10:
                digits[i - 1] += 1
                digits[i] -= 10
            else:
                break
            
        if digits[0] >= 10:
            digits[0] %= 10
            digits.insert(0, 1)
            
        return digits
        