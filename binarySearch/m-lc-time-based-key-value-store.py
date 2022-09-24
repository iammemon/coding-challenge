"""
 problem: https://leetcode.com/problems/time-based-key-value-store/submissions/
 pattern:
    - use dict to store key and array as it's value
    - use binary search to find the value
        - the right most true value (prev_time <= time)
            example time = 6  [2,4,8,9]
                               T T F F
"""


import collections
class TimeMap:

    def __init__(self):
        self.map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if not self.map[key]:
            return ""
        left = 0
        right = len(self.map[key]) - 1
        
        answer = ""
        while left<=right:
            mid = left + (right-left) // 2
            element = self.map[key][mid]
            if element[0] <= timestamp:
                answer = element[1]
                left = mid + 1 
            else:
                right = mid - 1
        return answer
                            
            
