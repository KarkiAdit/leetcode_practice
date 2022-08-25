# Mean of array after removing elements

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        sum = 0
        arr.sort()
        for i in range(int(len(arr)*0.05), int(len(arr)*0.95)):
            sum += arr[i]
        return sum/(len(arr)*0.9)
