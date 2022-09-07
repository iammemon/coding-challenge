"""
problem: https://leetcode.com/problems/online-stock-span/
pattern: next greater element to left
"""
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and price >= self.stack[-1][0]:
            span += self.stack.pop()[1]
        self.stack.append((price,span))
        return span



"""
practice problem

prices = [100,60,70,65,80,85]
# output = [1,1,2,1,4,5]

stack = []
result = []

for n in prices:
    span =1
    while stack and n >= stack[-1][0]:
        span+= stack.pop()[1]
    result.append(span)
    stack.append((n,span))
    
print(result)
"""