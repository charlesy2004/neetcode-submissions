class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_m = 0
        l_r = len(matrix) - 1
        lst = 0
        while l_m <= l_r:
            m = (l_m + l_r)//2
            if matrix[m][-1] < target:
                l_m = m + 1
            elif matrix[m][-1] >= target and matrix[m][0] <= target:
                lst = m
                break
            elif matrix[m][-1] > target:
                l_r = m - 1
        if m > len(matrix):
            return False
        l = 0
        r = len(matrix[lst]) - 1
        while l <= r:
            
            while l <= r:
                m = (l + r)//2
                if matrix[lst][m] < target:
                    l = m + 1
                elif matrix[lst][m] > target:
                    r = m - 1
                else:
                    return True
        return False
            
            
        