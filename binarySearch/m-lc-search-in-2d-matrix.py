"""
problem: https://leetcode.com/problems/search-a-2d-matrix/submissions/
pattern:

notice pattern the bottom element will be greater and the left will be smaller just like a binary search tree
    - start from top right corner of matrix
    - check curr element with target if found return true else continue
    - if target is greater go towards bottom which means next row
    - else on the left which means prev col
"""

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])
        row = 0
        col = cols - 1
        
        while row < rows and col > -1:
            curr = matrix[row][col]
            if curr == target:
                return True
            if target > curr:
                row+=1
            else:
                col-=1
        
        return False