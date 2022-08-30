# Sort the Matrix Diagonally

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        for i in range(len(mat)-1):
            x = i
            y = 0
            temp_mat = []
            while x <= len(mat)-1 and y <= len(mat[0])-1:
                print(x, y)
                temp_mat.append(mat[x][y])
                x += 1
                y += 1
            temp_mat.sort()
            x = i
            y = 0
            while x <= len(mat)-1 and y <= len(mat[0])-1:
                mat[x][y] = temp_mat[y]
                x += 1
                y += 1

        for j in range(1, len(mat[0])-1):
            x = 0
            y = j
            temp_mat = []
            while x <= len(mat)-1 and y <= len(mat[0])-1:
                temp_mat.append(mat[x][y])
                x += 1
                y += 1
            temp_mat.sort()
            x = 0
            y = j
            while x <= len(mat)-1 and y <= len(mat[0])-1:
                mat[x][y] = temp_mat[x]
                x += 1
                y += 1
        return mat
        Add the numbers
