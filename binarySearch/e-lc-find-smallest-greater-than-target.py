"""
problem: https://leetcode.com/problems/find-smallest-letter-greater-than-target/
pattern: ciel of element
    - move right if target is mid or greater than mid
    - when target is less than the mid,store the index of mid because it's a possible candidate 
"""


from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters)-1
        
        index = 0
        while left <= right:
            mid = left + (right-left)//2
            # letters contains duplicate so can't do `return mid+1`` when target element is match
            if target >= letters[mid]: #attention
                left = mid + 1 
            else:
                index = mid  #attention
                right = mid -1
            
            
            
        return letters[index]
            
            