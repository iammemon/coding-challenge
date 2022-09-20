"""
problem: https://leetcode.com/problems/find-a-peak-element-ii/submissions/
pattern: 
    - binary search on matrix col
    - calculate mid(col) and then find max element in that col
    - compare the adjacent cols of the max element 
    - if max is bigger than its adjacent than return it 
    - if not then move towards which has higher value
"""


from typing import List

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        left = 0
        right = cols - 1
        
        def findMaxInCol(col):
            # return max element row index in col             
            maxRow = 0
            for row in range(rows):
                if mat[row][col] > mat[maxRow][col]:
                    maxRow = row
            return maxRow
        
        while left<=right:
            mid = left + (right-left) // 2
            maxRow = findMaxInCol(mid)
            
            leftIsBig = mid > left and mat[maxRow][mid-1] > mat[maxRow][mid]
            rightIsBig = mid < right and mat[maxRow][mid+1] > mat[maxRow][mid]

            if not leftIsBig and not rightIsBig:
                return [maxRow,mid]
            if leftIsBig:
                right = mid - 1
            else:
                left = mid +1 
            
        return -1
            
