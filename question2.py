# Finding two sum target

# class Solution:

#     def twoSum(self, nums: List[int], target: int) -> List[int]:

#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i]+nums[j] == target:
#                     return [i, j]

# Optimized code in O(n) complexity
class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hash_map and i != hash_map[diff] != i:
                return [i, hash_map[diff]]
            else:
                hash_map[nums[i]] = i
