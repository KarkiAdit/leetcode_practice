# Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        current_prefix = strs[0]
        for i in range(1, len(strs)):
            while current_prefix != strs[i][0:len(current_prefix)]:
                current_prefix = current_prefix[:-1]
                if current_prefix == "":
                    return ""
        return current_prefix
