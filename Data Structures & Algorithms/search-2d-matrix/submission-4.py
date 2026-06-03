class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while l <= r:
            current = int((l + r)/2)
            if matrix[current][0] > target:
                r = current - 1
            elif matrix[current][-1] < target:
                l = current + 1
            else:
                left = 0
                right = len(matrix[current]) - 1
                while left <= right:
                    current1 = int((left + right) /2)
                    if matrix[current][current1] > target:
                        right = current1 - 1
                        
                    elif matrix[current][current1] < target:
                        left = current1 + 1
                    else:
                        return True
                return False
        return False
        
            
            
        