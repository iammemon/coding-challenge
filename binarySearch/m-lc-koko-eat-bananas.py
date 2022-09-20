"""
problem:https://leetcode.com/problems/koko-eating-bananas/
pattern: minimum page allocation
 - defined range 1 - maxPile (which is the max available in array koko can eat per hour)
 - we need to find the min in all possible answers so we use binary search on the range
 - check if the mid (speed) is enough to finish all piles in the given hour
 - if yes than store the answer and look for the min (move left)
 - if no then increase the speed (move right)
"""

import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)
        left = 1
        right = maxPile
        answer = maxPile
        
        def canEatAll(pilePerHour):
            totalHours = 0
            for pile in piles:
                # we are rounding up because any remainders means it will need 1 more hour to finish
                totalHours += math.ceil(pile/pilePerHour)
                if totalHours > h:
                    return False
            return True
        
        while left<=right:
            mid = left + (right-left)//2
            if(canEatAll(mid)):
                answer = mid
                right = mid -1
            else:
                left = mid + 1 
                
        return answer
    