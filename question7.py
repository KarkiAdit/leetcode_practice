# Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subString = ""
        currentHighest = 0

        for i in range(len(s)):
            if s[i:i+1] in subString:
                subString = subString[subString.index(s[i:i+1])+1:]+s[i:i+1]
            else:
                subString += s[i:i+1]
            if len(subString) > currentHighest:
                currentHighest = len(subString)

        return currentHighest
