class Solution(object):
    def reverseVowels(self, s):
        vowels = 'aeiouAEIOU'
        arr = []
        s = list(s)
        lens = len(s)
        
        for i in xrange(lens):
            if s[i] in vowels:
                arr.append(i)
                
        arrlens = len(arr)
        for i in xrange(arrlens / 2):
            s[arr[i]], s[arr[arrlens - i - 1]] = s[arr[arrlens - i - 1]], s[arr[i]]
            
        return ''.join(s)
            
            