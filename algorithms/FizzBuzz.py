class Solution(object):
    def fizzBuzz(self, n):
        fizzbuzz = []
        for i in xrange(n):
            if (i + 1) % 15 == 0:
                fizzbuzz.append("FizzBuzz")
            elif (i  + 1) % 3 == 0:
                fizzbuzz.append("Fizz")
            elif (i + 1) % 5 == 0:
                fizzbuzz.append("Buzz")
            else:
                fizzbuzz.append(str(i + 1))
        return fizzbuzz
                    
                    
                