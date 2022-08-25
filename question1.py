# Check if Number is a Sum of Powers of Three

class Solution:
    def isPowerOfThree(self, n: int):

        # x = 0
        # while 3**x <= n:
        #     if 3**x == n:
        #         return True
        #     x += 1
        # return False

        # if n == 0:
        #     return True
        # else:
        #     if n % 3 != 0:
        #         return False
        #     return self.isPowerOfThree(int(n/3))

        if n == 0:
            return False
        while n != 0 and n != 1:
            if n % 3 != 0:
                return False
            n = int(n/3)
        return True
