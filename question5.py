# Ransom note
# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         if len(magazine)< len(ransomNote): return False
#         Hashmap = {}
#         for i in magazine:
#             Hashmap[i] += 1
#             if i not in Hashmap:
#                 Hashmap[i]=1
#             else:
#                 Hashmap[i]+=1
#         for j in ransomNote:
#             if j in Hashmap and Hashmap[j] != 0:
#                 Hashmap[j] -= 1
#             else:
#                 return False
#         return True

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        item1 = collections.Counter(ransomNote)
        item2 = collections.Counter(magazine)
        for item, value in item1.items():
            if item not in item2 or item2[item] < value:
                return False
        return True
