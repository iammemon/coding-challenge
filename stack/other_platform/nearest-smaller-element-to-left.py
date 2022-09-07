# https://www.interviewbit.com/problems/nearest-smaller-element/#

class Solution:
	# @param A : list of integers
	# @return a list of integers
	def prevSmaller(self, A):
		
		result = [-1] * len(A)
		stack = []
		for i in range(len(A)):
			n = A[i]
			while stack and n <= stack[-1]:
				stack.pop()
			if stack:
				result[i] = stack[-1]
			stack.append(n)
		
		return result