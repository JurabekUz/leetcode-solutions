class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c:
            return mat

        new_mat = [[]]
        leng = 0
        for i in range(m):
            for j in range(n):
                if leng == c:
                    leng = 0
                    new_mat.append([])

                new_mat[-1].append(mat[i][j])
                leng += 1

        return new_mat
