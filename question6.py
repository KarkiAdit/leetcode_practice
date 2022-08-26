# Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        keyValues = {"I": 1, "V": 5, "X": 10,
                     "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = 0
        for i in range(len(s)-1):
            if keyValues[s[i:i+1]] < keyValues[s[i+1:i+2]]:
                sum -= keyValues[s[i:i+1]]
            else:
                sum += keyValues[s[i:i+1]]
            print(sum)

        return sum+keyValues[s[len(s)-1:]]
