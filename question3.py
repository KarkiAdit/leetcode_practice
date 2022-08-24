#  Find Valid Matrix Given Row and Column Sums

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        size1 = len(rowSum)
        size2 = len(colSum)
        i = 0
        j = 0
        arr = [size2*[0] for _ in range(size1)]

        while (i < size1 and j < size2):
            res = min(rowSum[i], colSum[j])
            arr[i][j] = res
            rowSum[i] -= res
            colSum[j] -= res
            if rowSum[i] == 0:
                i += 1
            if colSum[j] == 0:
                j += 1

        return arr
