class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        for i in range(len(matrix)):
            if target > matrix[i][len(matrix[i])-1]:
                continue
            else:
                l, r = 0, len(matrix[i])

                while l < r:
                    
                    mid = (l + r)//2
                    if matrix[i][mid] == target:
                        return True

                        
                    if target < matrix[i][mid]:
                        r = mid
                    else:
                        l = mid + 1
                    
        return False
            