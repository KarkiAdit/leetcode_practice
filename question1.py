# Check if Number is a Sum of Powers of Three

class Solution:
    def isPowerOfThree(self, n: int):
        x = 0

        while 3**x <= n:
            if 3**x == n:
                return True
            x += 1
        return False
